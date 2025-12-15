import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from reference.dependency_resolver import DependencyResolver

class TestCircularDirect(unittest.TestCase):
    def test_run(self):
        resolver = DependencyResolver()
        # Input: Direct cycle A <-> B
        data = {"A": ["B"], "B": ["A"]}
        result = resolver.resolve(data)
        
        self.assertFalse(result["success"])
        self.assertIsNotNone(result["error"])

if __name__ == '__main__':
    unittest.main()
