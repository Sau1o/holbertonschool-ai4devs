class DependencyResolver {
    /**
     * Resolves the build order using topological sort.
     * @param {Object} dependencies - Key: package name, Value: array of dependencies.
     * @returns {Object} - { success, build_order, error }
     */
    resolve(dependencies) {
        const inDegree = new Map();
        const graph = new Map();
        const allNodes = new Set(Object.keys(dependencies));

        // 1. Normalize: ensure all referenced deps are in allNodes
        for (const deps of Object.values(dependencies)) {
            deps.forEach(dep => allNodes.add(dep));
        }

        // Initialize data structures
        allNodes.forEach(node => {
            inDegree.set(node, 0);
            graph.set(node, []);
        });

        // 2. Build Graph (Dependency -> Dependent)
        // If A depends on B, B must precede A. Edge B -> A.
        for (const [pkg, deps] of Object.entries(dependencies)) {
            deps.forEach(dep => {
                graph.get(dep).push(pkg);
                inDegree.set(pkg, inDegree.get(pkg) + 1);
            });
        }

        // 3. Initialize Queue (using Array + sort for determinism)
        let queue = [];
        allNodes.forEach(node => {
            if (inDegree.get(node) === 0) {
                queue.push(node);
            }
        });
        
        // Sort initial queue for consistency with Python/Java
        queue.sort();

        const sortedOrder = [];

        // 4. Process Queue
        while (queue.length > 0) {
            // Simulate queue behavior: remove from front
            const current = queue.shift();
            sortedOrder.push(current);

            if (graph.has(current)) {
                const neighbors = graph.get(current);
                // Sort neighbors for consistency
                neighbors.sort();
                
                neighbors.forEach(neighbor => {
                    inDegree.set(neighbor, inDegree.get(neighbor) - 1);
                    if (inDegree.get(neighbor) === 0) {
                        queue.push(neighbor);
                    }
                });
                
                // After pushing new nodes, we must re-sort if we want strict
                // lexicographical processing order across the whole run,
                // but standard Kahn's just adds to end. 
                // To match the Python/Java PriorityQueue logic exactly:
                // We re-sort the queue after every insertion or just allow 
                // the natural "level" order. For strict parity with the Java 
                // PriorityQueue implementation above, we resort:
                queue.sort();
            }
        }

        // 5. Check for Cycles
        if (sortedOrder.length !== allNodes.size) {
            return {
                success: false,
                build_order: null,
                error: "Cycle detected or unresolvable dependencies."
            };
        }

        return {
            success: true,
            build_order: sortedOrder,
            error: null
        };
    }
}

module.exports = DependencyResolver;
