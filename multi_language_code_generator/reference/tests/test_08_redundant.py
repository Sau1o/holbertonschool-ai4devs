import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from reference.dependency_resolver import DependencyResolver

class TestRedundantDependencies(unittest.TestCase):
    def test_run(self):
        resolver = DependencyResolver()
        # Input: Duplicate dependency declaration
        data = {"A": ["B", "B"], "B": []}
        result = resolver.resolve(data)
        
        self.assertTrue(result["success"])
        self.assertEqual(result["build_order"], ["B", "A"])

if __name__ == '__main__':
    unittest.main()
