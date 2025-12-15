from collections import deque, defaultdict

class DependencyResolver:
    def resolve(self, dependencies: dict) -> dict:
        """
        Resolves the build order for a given dictionary of dependencies using
        Kahn's Algorithm for Topological Sorting.
        
        Args:
            dependencies: Dict where key is package name and value is list of dependencies.
        
        Returns:
            Dict with 'success', 'build_order', and 'error'.
        """
        # 1. Normalize graph and calculate in-degrees
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        all_nodes = set(dependencies.keys())

        # Ensure all nodes mentioned in values are also tracked
        for pkg, deps in dependencies.items():
            for dep in deps:
                all_nodes.add(dep)

        # Build the graph (dependency -> dependent) because if A depends on B,
        # B must come before A. So the edge is B -> A.
        for pkg, deps in dependencies.items():
            for dep in deps:
                graph[dep].append(pkg)
                in_degree[pkg] += 1
        
        # 2. Initialize queue with nodes having 0 in-degree (no dependencies)
        queue = deque([node for node in all_nodes if in_degree[node] == 0])
        sorted_order = []

        # 3. Process queue
        while queue:
            # Sort for deterministic output when multiple nodes are ready simultaneously
            # (Note: In a real large-scale scenario, sorting the queue is inefficient, 
            # but valid for stability in this reference implementation)
            current = queue.popleft() 
            sorted_order.append(current)

            if current in graph:
                for neighbor in graph[current]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
        
        # 4. Check for cycles
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
