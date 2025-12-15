import java.util.*;

public class DependencyResolver {

    // Simple DTO for the result to match JSON structure
    public static class ResolutionResult {
        public boolean success;
        public List<String> build_order;
        public String error;

        public ResolutionResult(boolean success, List<String> build_order, String error) {
            this.success = success;
            this.build_order = build_order;
            this.error = error;
        }
    }

    public ResolutionResult resolve(Map<String, List<String>> dependencies) {
        Map<String, Integer> inDegree = new HashMap<>();
        Map<String, List<String>> graph = new HashMap<>();
        Set<String> allNodes = new HashSet<>(dependencies.keySet());

        // 1. Normalize and Identify all nodes
        for (List<String> deps : dependencies.values()) {
            allNodes.addAll(deps);
        }

        // Initialize in-degree for all nodes to 0
        for (String node : allNodes) {
            inDegree.put(node, 0);
            graph.put(node, new ArrayList<>());
        }

        // 2. Build Graph (Edge: Dependency -> Dependent)
        // If A depends on B (A -> B), we need B before A.
        // So in our graph for topo sort: B -> A.
        for (Map.Entry<String, List<String>> entry : dependencies.entrySet()) {
            String pkg = entry.getKey();
            List<String> deps = entry.getValue();
            
            for (String dep : deps) {
                graph.get(dep).add(pkg);
                inDegree.put(pkg, inDegree.get(pkg) + 1);
            }
        }

        // 3. Initialize Queue with 0 in-degree nodes
        // PriorityQueue used to ensure deterministic output (lexicographical order)
        PriorityQueue<String> queue = new PriorityQueue<>();
        for (String node : allNodes) {
            if (inDegree.get(node) == 0) {
                queue.add(node);
            }
        }

        List<String> sortedOrder = new ArrayList<>();

        // 4. Process Queue
        while (!queue.isEmpty()) {
            String current = queue.poll();
            sortedOrder.add(current);

            List<String> neighbors = graph.get(current);
            // Sort neighbors strictly for deterministic output across languages
            Collections.sort(neighbors); 
            
            for (String neighbor : neighbors) {
                inDegree.put(neighbor, inDegree.get(neighbor) - 1);
                if (inDegree.get(neighbor) == 0) {
                    queue.add(neighbor);
                }
            }
        }

        // 5. Check for Cycles
        if (sortedOrder.size() != allNodes.size()) {
            return new ResolutionResult(false, null, "Cycle detected or unresolvable dependencies.");
        }

        return new ResolutionResult(true, sortedOrder, null);
    }
}
