import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from reference.dependency_resolver import DependencyResolver

class TestSelfDependency(unittest.TestCase):
    def test_run(self):
        resolver = DependencyResolver()
        # Input: A depends on itself
        data = {"A": ["A"]}
        result = resolver.resolve(data)
        
        self.assertFalse(result["success"])

if __name__ == '__main__':
    unittest.main()
