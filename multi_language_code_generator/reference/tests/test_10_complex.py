import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from reference.dependency_resolver import DependencyResolver

class TestComplexStructure(unittest.TestCase):
    def test_run(self):
        resolver = DependencyResolver()
        # Input: Multi-level graph
        data = {
            "Dashboard": ["Widget", "Auth"],
            "Widget": ["Charts", "Styles"],
            "Charts": ["D3"],
            "Auth": ["Styles", "DB"],
            "Styles": [], "DB": [], "D3": []
        }
        result = resolver.resolve(data)
        
        self.assertTrue(result["success"])
        order = result["build_order"]
        self.assertTrue(order.index("D3") < order.index("Charts"))
        self.assertTrue(order.index("Styles") < order.index("Widget"))
        self.assertTrue(order.index("Widget") < order.index("Dashboard"))

if __name__ == '__main__':
    unittest.main()
