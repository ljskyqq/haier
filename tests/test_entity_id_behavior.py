import ast
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class EntityIdSourceTests(unittest.TestCase):
    def test_entity_does_not_force_unique_id_as_entity_id(self):
        source = (ROOT / "custom_components/haier/entity.py").read_text(
            encoding="utf-8"
        )
        tree = ast.parse(source)
        assignments = [
            node
            for node in ast.walk(tree)
            if isinstance(node, (ast.Assign, ast.AnnAssign))
        ]
        self.assertFalse(
            any("self.entity_id" in ast.unparse(node) for node in assignments)
        )


if __name__ == "__main__":
    unittest.main()
