import unittest
import sys
import os

# Adjust path to import the resolver
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dependency_resolver import DependencyResolver

class TestDependencyResolver(unittest.TestCase):
    def setUp(self):
        self.resolver = DependencyResolver()

    def test_01_simple_chain(self):
        data = {"A": ["B"], "B": ["C"], "C": []}
        result = self.resolver.resolve(data)
        self.assertTrue(result["success"])
        self.assertEqual(result["build_order"], ["C", "B", "A"])

    def test_02_diamond_dependency(self):
        data = {"App": ["Lib1", "Lib2"], "Lib1": ["Core"], "Lib2": ["Core"], "Core": []}
        result = self.resolver.resolve(data)
        self.assertTrue(result["success"])
        # Core needs to be first, App last. Lib1/Lib2 order doesn't matter relative to each other.
        order = result["build_order"]
        self.assertEqual(order[0], "Core")
        self.assertEqual(order[-1], "App")
        self.assertIn("Lib1", order[1:3])
        self.assertIn("Lib2", order[1:3])

    def test_03_circular_dependency_direct(self):
        data = {"A": ["B"], "B": ["A"]}
        result = self.resolver.resolve(data)
        self.assertFalse(result["success"])
        self.assertIsNotNone(result["error"])

    def test_04_circular_dependency_indirect(self):
        data = {"A": ["B"], "B": ["C"], "C": ["A"]}
        result = self.resolver.resolve(data)
        self.assertFalse(result["success"])

    def test_05_disconnected_graphs(self):
        data = {"A": ["B"], "B": [], "X": ["Y"], "Y": []}
        result = self.resolver.resolve(data)
        self.assertTrue(result["success"])
        order = result["build_order"]
        # Check relative ordering
        self.assertTrue(order.index("B") < order.index("A"))
        self.assertTrue(order.index("Y") < order.index("X"))
        self.assertEqual(len(order), 4)

    def test_06_empty_input(self):
        data = {}
        result = self.resolver.resolve(data)
        self.assertTrue(result["success"])
        self.assertEqual(result["build_order"], [])

    def test_07_self_dependency(self):
        data = {"A": ["A"]}
        result = self.resolver.resolve(data)
        self.assertFalse(result["success"])

    def test_08_redundant_dependencies(self):
        # A depends on B twice
        data = {"A": ["B", "B"], "B": []}
        result = self.resolver.resolve(data)
        self.assertTrue(result["success"])
        self.assertEqual(result["build_order"], ["B", "A"])

    def test_09_implicit_dependency(self):
        # "B" is not a key, but referenced. Should be treated as a leaf.
        data = {"A": ["B"]}
        result = self.resolver.resolve(data)
        self.assertTrue(result["success"])
        self.assertEqual(result["build_order"], ["B", "A"])

    def test_10_complex_web(self):
        data = {
            "Web": ["Auth", "DB"],
            "Auth": ["Utils", "DB"],
            "DB": ["OS"],
            "Utils": ["OS"],
            "OS": []
        }
        result = self.resolver.resolve(data)
        self.assertTrue(result["success"])
        order = result["build_order"]
        self.assertEqual(order[0], "OS") # OS has no deps
        self.assertTrue(order.index("DB") > order.index("OS"))
        self.assertTrue(order.index("Utils") > order.index("OS"))
        self.assertTrue(order.index("Auth") > order.index("Utils"))
        self.assertTrue(order.index("Auth") > order.index("DB"))
        self.assertTrue(order.index("Web") > order.index("Auth"))

if __name__ == '__main__':
    unittest.main()
