from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
README_PATH = REPO_ROOT / "README.md"


class TestRepositoryBlueprint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme_text = README_PATH.read_text(encoding="utf-8")

    def test_readme_exists(self):
        self.assertTrue(README_PATH.exists(), "README.md must exist at repository root")

    def test_core_sections_present(self):
        required_sections = [
            "# AETHER Render Engine: Full-Stack Blueprint",
            "## Core Goal",
            "## Architecture",
            "## Repository Layout",
            "## Service Blueprint",
            "## AADT Operational Loop",
            "## End-to-End Mapping",
            "## Outcome",
        ]
        for section in required_sections:
            with self.subTest(section=section):
                self.assertIn(section, self.readme_text)

    def test_frontend_and_backend_blueprint_present(self):
        self.assertIn("### 01_frontend", self.readme_text)
        self.assertIn("### 02_backend_api", self.readme_text)

    def test_core_service_blueprint_entries_present(self):
        required_services = [
            "#### nlp_parser",
            "#### asset_synthesizer",
            "#### motion_director",
            "#### rendering_core",
            "#### twin_behavioral_model",
        ]
        for service in required_services:
            with self.subTest(service=service):
                self.assertIn(service, self.readme_text)

    def test_data_layer_blueprint_entries_present(self):
        required_data_components = [
            "#### graph_db",
            "#### sensor_data_lake",
            "#### metadata_service",
        ]
        for component in required_data_components:
            with self.subTest(component=component):
                self.assertIn(component, self.readme_text)

    def test_ari_reference_present(self):
        self.assertIn("Agency Resistance Index (ARI)", self.readme_text)

    def test_top_level_directories_exist(self):
        expected_dirs = [
            "01_frontend",
            "02_backend_api",
            "03_core_services",
            "04_data_layer",
            "05_simulation_utils",
            "deployment",
        ]
        for rel_dir in expected_dirs:
            with self.subTest(directory=rel_dir):
                path = REPO_ROOT / rel_dir
                self.assertTrue(path.exists(), f"{rel_dir} should exist")
                self.assertTrue(path.is_dir(), f"{rel_dir} should be a directory")

    def test_core_service_directories_exist(self):
        expected_dirs = [
            "03_core_services/nlp_parser",
            "03_core_services/asset_synthesizer",
            "03_core_services/motion_director",
            "03_core_services/rendering_core",
            "03_core_services/twin_behavioral_model",
        ]
        for rel_dir in expected_dirs:
            with self.subTest(directory=rel_dir):
                path = REPO_ROOT / rel_dir
                self.assertTrue(path.exists(), f"{rel_dir} should exist")
                self.assertTrue(path.is_dir(), f"{rel_dir} should be a directory")

    def test_data_layer_directories_exist(self):
        expected_dirs = [
            "04_data_layer/graph_db",
            "04_data_layer/sensor_data_lake",
            "04_data_layer/metadata_service",
        ]
        for rel_dir in expected_dirs:
            with self.subTest(directory=rel_dir):
                path = REPO_ROOT / rel_dir
                self.assertTrue(path.exists(), f"{rel_dir} should exist")
                self.assertTrue(path.is_dir(), f"{rel_dir} should be a directory")

    def test_simulation_utils_directories_exist(self):
        expected_dirs = [
            "05_simulation_utils/affective_math",
            "05_simulation_utils/utils",
        ]
        for rel_dir in expected_dirs:
            with self.subTest(directory=rel_dir):
                path = REPO_ROOT / rel_dir
                self.assertTrue(path.exists(), f"{rel_dir} should exist")
                self.assertTrue(path.is_dir(), f"{rel_dir} should be a directory")


if __name__ == "__main__":
    unittest.main()
