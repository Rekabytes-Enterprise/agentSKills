"""Regression tests for the dependency-free skill package validator."""

import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import validate_library


class SkillValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def make_skill(self, name="example", folder=None, description='"A portable example skill."', body=""):
        skill = self.root / "skills" / (folder or name)
        skill.mkdir(parents=True, exist_ok=True)
        (skill / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: {description}\n---\n\n# Example\n\n{body}",
            encoding="utf-8",
        )
        return skill

    def errors(self):
        return validate_library(self.root)

    def assert_error(self, fragment):
        self.assertTrue(any(fragment in error for error in self.errors()), self.errors())

    def test_valid_skill_and_local_reference(self):
        skill = self.make_skill(body="[Guide](references/guide.md#overview)")
        (skill / "references").mkdir()
        (skill / "references" / "guide.md").write_text("# Overview\n", encoding="utf-8")
        self.assertEqual([], self.errors())

    def test_no_skills_directory(self):
        self.assert_error("missing skills/ directory")

    def test_empty_skills_directory(self):
        (self.root / "skills").mkdir()
        self.assert_error("no skill folders found")

    def test_folder_missing_entrypoint(self):
        (self.root / "skills" / "example").mkdir(parents=True)
        self.assert_error("missing SKILL.md")

    def test_invalid_skill_name(self):
        self.make_skill(name="bad--name")
        self.assert_error("single hyphens")

    def test_name_must_match_directory(self):
        self.make_skill(folder="different")
        self.assert_error("name must match folder")

    def test_missing_description(self):
        skill = self.make_skill()
        (skill / "SKILL.md").write_text("---\nname: example\n---\n# Example\n", encoding="utf-8")
        self.assert_error("missing description")

    def test_empty_description(self):
        self.make_skill(description='""')
        self.assert_error("nonempty string")

    def test_description_length_limit(self):
        self.make_skill(description='"' + "x" * 1025 + '"')
        self.assert_error("exceeds 1024 characters")

    def test_duplicate_metadata(self):
        skill = self.make_skill()
        (skill / "SKILL.md").write_text(
            '---\nname: example\nname: example\ndescription: "Example"\n---\n', encoding="utf-8"
        )
        self.assert_error("duplicate name")

    def test_multiline_description_rejected_by_repository_convention(self):
        self.make_skill(description="|")
        self.assert_error("single-line value")

    def test_missing_link_target(self):
        self.make_skill(body="[Missing](references/missing.md)")
        self.assert_error("missing local link target")

    def test_links_must_stay_inside_skill_package(self):
        (self.root / "README.md").write_text("# Library\n", encoding="utf-8")
        self.make_skill(body="[Outside](../../README.md)")
        self.assert_error("escapes its portable package")

    def test_output_template_placeholders_are_allowed(self):
        self.make_skill(body="[Generated PRD]({{MASTER_PRD_LINK}})")
        self.assertEqual([], self.errors())

    def test_fenced_and_inline_code_are_not_links(self):
        self.make_skill(body="```markdown\n[Example](missing.md)\n```\n`[Example](missing.md)`\n")
        self.assertEqual([], self.errors())

    def test_reference_style_link_targets_are_checked(self):
        self.make_skill(body="[Guide][guide]\n\n[guide]: references/missing.md\n")
        self.assert_error("missing local link target")

    def test_external_urls_and_fragment_links_are_allowed(self):
        self.make_skill(body="[Web](https://example.com/docs) [Email](mailto:test@example.com) [Here](#example)")
        self.assertEqual([], self.errors())

    def test_absolute_local_links_are_rejected(self):
        self.make_skill(body="[Private](/private/guide.md)")
        self.assert_error("local link must be relative")

    def test_multiple_skills_are_discovered(self):
        self.make_skill()
        self.make_skill(name="another-skill")
        self.assertEqual([], self.errors())


if __name__ == "__main__":
    unittest.main()
