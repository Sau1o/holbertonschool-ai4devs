import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from reference.dependency_resolver import DependencyResolver

class TestDiamondDependency(unittest.TestCase):
    def test_run(self):
        resolver = DependencyResolver()
        # Input: App depends on Lib1 & Lib2, both depend on Core
        data = {"App": ["Lib1", "Lib2"], "Lib1": ["Core"], "Lib2": ["Core"], "Core": []}
        result = resolver.resolve(data)
        
        self.assertTrue(result["success"])
        order = result["build_order"]
        self.assertEqual(order[0], "Core")
        self.assertEqual(order[-1], "App")
        self.assertIn("Lib1", order[1:3])
        self.assertIn("Lib2", order[1:3])

if __name__ == '__main__':
    unittest.main()
