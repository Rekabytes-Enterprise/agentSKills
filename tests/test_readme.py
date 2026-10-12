"""Offline README markup, installation, and truthful-metric contracts."""

import re
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from scripts.validate_skills import without_code


ROOT = Path(__file__).resolve().parents[1]


class ReadmeMarkup(HTMLParser):
    TRACKED = {"div", "p", "a", "details", "summary", "strong", "h1", "sub"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag in self.TRACKED:
            self.stack.append(tag)
        if tag == "a":
            self.links.append(attributes.get("href", ""))
        if tag == "img":
            self.images.append(attributes)

    def handle_endtag(self, tag):
        if tag not in self.TRACKED:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"Unexpected closing tag: {tag}")
        else:
            self.stack.pop()


class ReadmeContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.markup = ReadmeMarkup()
        cls.markup.feed(without_code(cls.text))
        cls.markup.close()

    def test_primary_install_command_stays_bare(self):
        match = re.search(r"## Quick start\s+.*?```bash\n(.*?)\n```", self.text, re.DOTALL)
        self.assertIsNotNone(match)
        self.assertEqual("npx skills add Rekabytes-Enterprise/agentSKills", match.group(1).strip())
        self.assertNotIn("--skill", self.text)
        self.assertNotIn("--all", self.text)

    def test_install_badge_uses_documented_native_endpoint(self):
        badges = [image for image in self.markup.images if image.get("src", "").startswith("https://skills.sh/b/")]
        self.assertEqual(1, len(badges))
        self.assertEqual("https://skills.sh/b/rekabytes-enterprise/agentskills", badges[0]["src"])
        self.assertNotIn("img.shields.io/npm/", self.text)

    def test_metric_scope_and_telemetry_opt_out_are_explicit(self):
        for phrase in ("not unique users", "does not count these installations", "DISABLE_TELEMETRY", "DO_NOT_TRACK", "publication, indexing, and reported usage", "no custom install hooks or analytics scripts"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.text)

    def test_html_containers_are_balanced(self):
        self.assertEqual([], self.markup.errors)
        self.assertEqual([], self.markup.stack)

    def test_html_images_have_accessible_labels(self):
        self.assertTrue(self.markup.images)
        for image in self.markup.images:
            self.assertTrue(image.get("src"))
            self.assertTrue(image.get("alt", "").strip())

    def test_navigation_fragments_and_local_html_targets_resolve(self):
        headings = re.findall(r"^#{1,6}\s+(.+)$", self.text, re.MULTILINE)
        slugs = {re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-") for heading in headings}
        for target in self.markup.links + [image["src"] for image in self.markup.images]:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            with self.subTest(target=target):
                if parsed.path:
                    self.assertTrue((ROOT / unquote(parsed.path)).exists())
                elif parsed.fragment:
                    self.assertIn(parsed.fragment, slugs)

    def test_banner_is_accessible_static_svg_without_external_dependencies(self):
        banner = ROOT / "docs" / "assets" / "readme-banner.svg"
        element = ET.parse(banner).getroot()
        ns = {"svg": "http://www.w3.org/2000/svg"}
        self.assertEqual("0 0 1280 360", element.attrib["viewBox"])
        self.assertEqual("img", element.attrib["role"])
        self.assertIsNotNone(element.find("svg:title", ns))
        self.assertIsNotNone(element.find("svg:desc", ns))
        for node in element.iter():
            self.assertNotIn(node.tag.split("}")[-1], {"script", "foreignObject", "image", "animate", "animateMotion", "animateTransform"})
            for name, value in node.attrib.items():
                if name.split("}")[-1] == "href":
                    self.assertTrue(value.startswith("#"))


if __name__ == "__main__":
    unittest.main()
