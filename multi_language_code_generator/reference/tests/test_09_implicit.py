import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from reference.dependency_resolver import DependencyResolver

class TestImplicitDependency(unittest.TestCase):
    def test_run(self):
        resolver = DependencyResolver()
        # Input: "Utils" is referenced but not a key
        data = {"App": ["Utils"]}
        result = resolver.resolve(data)
        
        self.assertTrue(result["success"])
        self.assertEqual(result["build_order"], ["Utils", "App"])

if __name__ == '__main__':
    unittest.main()
