import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from reference.dependency_resolver import DependencyResolver

class TestDisconnectedGraphs(unittest.TestCase):
    def test_run(self):
        resolver = DependencyResolver()
        # Input: Two independent clusters
        data = {"Front": ["UI"], "UI": [], "Back": ["DB"], "DB": []}
        result = resolver.resolve(data)
        
        self.assertTrue(result["success"])
        order = result["build_order"]
        self.assertTrue(order.index("UI") < order.index("Front"))
        self.assertTrue(order.index("DB") < order.index("Back"))

if __name__ == '__main__':
    unittest.main()
