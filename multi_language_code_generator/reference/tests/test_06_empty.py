import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from reference.dependency_resolver import DependencyResolver

class TestEmptyInput(unittest.TestCase):
    def test_run(self):
        resolver = DependencyResolver()
        # Input: Empty JSON
        data = {}
        result = resolver.resolve(data)
        
        self.assertTrue(result["success"])
        self.assertEqual(result["build_order"], [])

if __name__ == '__main__':
    unittest.main()
