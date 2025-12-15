# /reference/tests/test_01_simple_chain.py
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from reference.dependency_resolver import DependencyResolver

class TestSimpleChain(unittest.TestCase):
    def test_run(self):
        resolver = DependencyResolver()
        # Input: A depends on B, B depends on C
        data = {"A": ["B"], "B": ["C"], "C": []}
        result = resolver.resolve(data)
        
        self.assertTrue(result["success"])
        self.assertEqual(result["build_order"], ["C", "B", "A"])

if __name__ == '__main__':
    unittest.main()
