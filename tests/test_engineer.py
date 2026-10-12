"""Static engineer skill/template contracts, not live agent behavior tests."""

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import validate_library


SKILL_ROOT = Path(__file__).resolve().parents[1] / "skills" / "engineer"


class EngineerContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.research = (SKILL_ROOT / "references" / "stack-research.md").read_text(encoding="utf-8")
        cls.engineering = (SKILL_ROOT / "references" / "engineering.md").read_text(encoding="utf-8")
        cls.architecture = (SKILL_ROOT / "references" / "architecture.md").read_text(encoding="utf-8")
        cls.production = (SKILL_ROOT / "references" / "production.md").read_text(encoding="utf-8")
        cls.client = (SKILL_ROOT / "references" / "client-design.md").read_text(encoding="utf-8")
        cls.admin = (SKILL_ROOT / "references" / "admin-design.md").read_text(encoding="utf-8")
        cls.profile = (SKILL_ROOT / "templates" / "project-profile.md").read_text(encoding="utf-8")

    def test_skill_is_portable_when_copied_on_its_own(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(SKILL_ROOT, root / "skills" / "engineer")
            self.assertEqual([], validate_library(root))

    def test_approval_stop_precedes_saving_configuration(self):
        proposal = self.skill.index("### 3. Present the compatibility proposal and STOP")
        stop = self.skill.index("**STOP here.**", proposal)
        save = self.skill.index("### 4. Save approved project configuration")
        self.assertLess(proposal, stop)
        self.assertLess(stop, save)
        self.assertIn("Only after approval", self.skill[save:])

    def test_profile_is_project_local_even_with_global_installation(self):
        self.assertIn("docs/development/engineer-profile.md", self.skill)
        self.assertIn("Do not rewrite this library, an installed `SKILL.md`, or a shared global installation", self.skill)
        self.assertIn("even if engineer was installed globally", self.skill)

    def test_later_uses_recheck_configuration_and_require_refresh_approval(self):
        self.assertIn("Read that profile on every use", self.skill)
        self.assertIn("Compare profile assumptions against manifests/lockfiles", self.skill)
        self.assertIn("ask for approval before updating the profile", self.skill)

    def test_configuration_does_not_authorize_implementation_or_upgrades(self):
        self.assertIn("Configuration approval alone does not start development", self.skill)
        self.assertIn("A separate explicit implementation request", self.skill)
        self.assertIn("Never install/upgrade packages", self.skill)
        self.assertIn("newest major version", self.skill)

    def test_state_research_distinguishes_frameworks_and_build_tools(self):
        for setup in ("Vite + React", "Vite + Vue", "Laravel + Blade", "Laravel + Livewire", "Laravel + Inertia", "Plain PHP"):
            with self.subTest(setup=setup):
                self.assertIn(setup, self.research)
        self.assertIn("Laravel and Vite can coexist", self.research)
        self.assertIn("no additional state library", self.research)

    def test_original_jotai_utilities_remain_conditional(self):
        self.assertIn("only when the profile selects it", self.engineering)
        for api in ("useAtomValue", "useSetAtom", "useAtom", "atomWithStorage", "createJSONStorage", "atomWithReset", "useResetAtom", "RESET", "loadable", "unwrap", "atomWithObservable"):
            with self.subTest(api=api):
                self.assertIn(f"`{api}`", self.engineering)

    def test_client_recipe_retains_palette_geometry_and_review_sizes(self):
        for value in ("#0f172a", "#64748b", "#6366f1", "0.72/0.55", "0.92rem", "18px", "11px", "10px", "260px", "280px", "800px", "1280/1440/1600/1920"):
            with self.subTest(value=value):
                self.assertIn(value, self.client)
        self.assertIn("Intentionally inactive controls do not authorize new features", self.client)

    def test_admin_recipe_retains_fonts_palette_and_distinct_geometry(self):
        for value in ("Instrument Sans", "IBM Plex Mono", "#f4f5f5", "#232626", "#636b6b", "#a63e24", "400", "500", "2px", "4px", "1280/1440/1600/1920"):
            with self.subTest(value=value):
                self.assertIn(value, self.admin)
        self.assertIn("Do not propagate console typography", self.admin)
        self.assertIn("fixture/sample data explicitly", self.admin)

    def test_profile_records_compatibility_evidence_and_refresh(self):
        for section in ("Identity, scope, and approval", "Actual stack and compatibility evidence", "State ownership map", "Surface-specific design and motion", "Verification and evidence plan", "Refresh and decision record"):
            with self.subTest(section=section):
                self.assertIn(section, self.profile)
        self.assertIn("Approved for the recorded configuration scope", self.profile)

    def test_provider_calls_stay_outside_open_transactions(self):
        for reference in (self.architecture, self.production):
            self.assertIn("Keep external provider calls outside open database transactions", reference)

    def test_render_boundaries_do_not_replace_action_error_handling(self):
        self.assertIn("A render error boundary does not replace async-event/action handling", self.engineering)
        self.assertIn("render-error boundaries", self.profile)

    def test_hono_recipe_preserves_route_inference_when_selected(self):
        self.assertIn("If Hono is selected", self.architecture)
        self.assertIn("`app.route()`", self.architecture)
        self.assertIn("preserve route inference", self.architecture)
        self.assertIn("typed handler factories", self.architecture)

    def test_production_proxy_lifecycle_and_release_rules_are_retained(self):
        for rule in ("reverse-proxy", "stop accepting new work", "bounded request draining", "close workers/connections deliberately", "pin release images", "verify staging acceptance"):
            with self.subTest(rule=rule):
                self.assertIn(rule, self.production)

    def test_prd_approvals_tracking_sync_and_regression_reopening(self):
        self.assertIn("master and selected phase PRD/UAT revisions", self.skill)
        self.assertIn("Synchronize the development index, master PRD, affected phase PRD", self.skill)
        self.assertIn("Reopen affected checks", self.skill)
        self.assertIn("UAT execution and user sign-off remain separate", self.skill)

    def test_skill_has_no_private_machine_paths(self):
        for path in SKILL_ROOT.rglob("*.md"):
            with self.subTest(path=path.name):
                text = path.read_text(encoding="utf-8")
                self.assertNotIn("/Volumes/", text)
                self.assertNotIn("/Users/", text)
                self.assertNotIn("@mokara/", text)


if __name__ == "__main__":
    unittest.main()
