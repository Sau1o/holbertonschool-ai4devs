from collections import deque, defaultdict
import json

class DependencyResolver:
    def resolve(self, dependencies: dict) -> dict:
        """
        Resolves build order using Kahn's Algorithm.
        """
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        all_nodes = set(dependencies.keys())

        # Normalize graph: Ensure all referenced nodes exist in set
        for pkg, deps in dependencies.items():
            for dep in deps:
                all_nodes.add(dep)

        # Build graph: dependent -> dependency (reversed logic for build order)
        # However, for "install dependencies first", if A depends on B:
        # We need B before A. Edge: B -> A.
        for pkg, deps in dependencies.items():
            for dep in deps:
                graph[dep].append(pkg)
                in_degree[pkg] += 1
        
        # Initialize queue with nodes having 0 dependencies
        queue = deque([node for node in all_nodes if in_degree[node] == 0])
        
        # Sort initial queue for deterministic output in tests
        # Note: deque doesn't support sort directly, so we sort a list then make a deque
        sorted_start = sorted(list(queue))
        queue = deque(sorted_start)
        
        sorted_order = []

        while queue:
            current = queue.popleft()
            sorted_order.append(current)

            if current in graph:
                # Sort neighbors for deterministic behavior
                neighbors = sorted(graph[current])
                for neighbor in neighbors:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
        
        if len(sorted_order) != len(all_nodes):
            return {
                "success": False,
                "build_order": None,
                "error": "Cycle detected or unresolvable dependencies."
            }

        return {
            "success": True,
            "build_order": sorted_order,
            "error": None
        }
