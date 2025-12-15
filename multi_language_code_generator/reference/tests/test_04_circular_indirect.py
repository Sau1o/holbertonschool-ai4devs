import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from reference.dependency_resolver import DependencyResolver

class TestCircularIndirect(unittest.TestCase):
    def test_run(self):
        resolver = DependencyResolver()
        # Input: Indirect cycle A -> B -> C -> A
        data = {"A": ["B"], "B": ["C"], "C": ["A"]}
        result = resolver.resolve(data)
        
        self.assertFalse(result["success"])
        self.assertIn("Cycle", str(result["error"]))

if __name__ == '__main__':
    unittest.main()
