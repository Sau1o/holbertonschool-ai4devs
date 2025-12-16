import unittest
import sys
import os

# Ajusta o path para importar a implementação da Lista 3
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../implementations/python')))
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
        order = result["build_order"]
        self.assertEqual(order[0], "Core")
        self.assertEqual(order[-1], "App")
        # Verifica se Lib1 e Lib2 estão no meio (índices 1 e 2)
        middle = sorted(order[1:3])
        self.assertEqual(middle, ["Lib1", "Lib2"])

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
        data = {"Front": ["UI"], "UI": [], "Back": ["DB"], "DB": []}
        result = self.resolver.resolve(data)
        self.assertTrue(result["success"])
        order = result["build_order"]
        self.assertTrue(order.index("UI") < order.index("Front"))
        self.assertTrue(order.index("DB") < order.index("Back"))

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
        data = {"A": ["B", "B"], "B": []}
        result = self.resolver.resolve(data)
        self.assertTrue(result["success"])
        self.assertEqual(result["build_order"], ["B", "A"])

    def test_09_implicit_dependency(self):
        data = {"App": ["Utils"]}
        result = self.resolver.resolve(data)
        self.assertTrue(result["success"])
        self.assertEqual(result["build_order"], ["Utils", "App"])

    def test_10_complex_structure(self):
        data = {
            "Dashboard": ["Widget", "Auth"],
            "Widget": ["Charts", "Styles"],
            "Charts": ["D3"],
            "Auth": ["Styles", "DB"],
            "Styles": [], "DB": [], "D3": []
        }
        result = self.resolver.resolve(data)
        self.assertTrue(result["success"])
        order = result["build_order"]
        self.assertTrue(order.index("D3") < order.index("Charts"))
        self.assertTrue(order.index("Styles") < order.index("Widget"))
        self.assertTrue(order.index("Widget") < order.index("Dashboard"))

if __name__ == '__main__':
    unittest.main()
