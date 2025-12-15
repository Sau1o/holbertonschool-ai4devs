# Cross-Language Specification - Package Dependency Resolver

## Algorithm Description
The algorithm implements a **Topological Sort** to resolve dependencies for a software package manager. It models the packages and their dependencies as a Directed Graph where:
- Nodes represent packages.
- Edges represent a "depends on" relationship.

The goal is to produce a linear ordering of packages such that for every dependency $U \to V$ (Package U depends on Package V), V comes before U in the ordering. The algorithm must also detect cycles (circular dependencies) and report them as errors, as these make resolution impossible.

## Inputs
- **Format:** JSON Object.
- **Structure:** Key-Value pairs where the Key is the `package_name` (string) and the Value is a list of `dependencies` (array of strings).
- **Example:** `{"pkgA": ["pkgB", "pkgC"], "pkgB": []}`

## Outputs
- **Format:** JSON Object.
- **Structure:**
  - `success`: Boolean (true if sorted, false if cycle detected).
  - `build_order`: Array of strings (the sorted installation list) or `null` if failed.
  - `error`: String description of the error (e.g., "Cycle detected") or `null`.

## Edge Cases
1.  **Empty Input:** An empty JSON object should return an empty build order.
2.  **Self-Dependency:** A package depending on itself (`"A": ["A"]`).
3.  **Complex Cycles:** Indirect cycles involving multiple nodes (`A->B->C->A`).
4.  **Disconnected Graphs:** Multiple clusters of packages that do not relate to each other (should still be sorted into a valid single list).
5.  **Redundant Dependencies:** A package listed multiple times in a dependency array.

## Test Cases

### Test Case 1: Simple Chain (Linear)
**Input:**
```json
{
  "frontend": ["api"],
  "api": ["db"],
  "db": []
}
```

**expected Output:**
```json
{
  "success": true,
  "build_order": ["db", "api", "frontend"],
  "error": null
}
```

### Test Case 2: Diamond Dependency (Shared Core)
**Input:**
```json
{
  "app": ["lib_x", "lib_y"],
  "lib_x": ["core"],
  "lib_y": ["core"],
  "core": []
}
```
**Expected Output:**
```json
{
  "success": true,
  "build_order": ["core", "lib_x", "lib_y", "app"],
  "error": null
}
```
*(Note: `lib_x` and `lib_y` order may vary, but both must appear after `core` and before `app`).*

### Test Case 3: Circular Dependency (Failure)
**Input:**
```json
{
  "A": ["B"],
  "B": ["C"],
  "C": ["A"]
}
```
**Expected Output:**
```json
{
  "success": false,
  "build_order": null,
  "error": "Cycle detected"
}
```

### Test Case 4: Independent Groups (Disconnected)
**Input:**
```json
{
  "tools": ["utils"],
  "utils": [],
  "game": ["engine"],
  "engine": []
}
```
**Expected Output:**
```json
{
  "success": true,
  "build_order": ["utils", "tools", "engine", "game"],
  "error": null
}
```

### Test Case 5: Empty Project
**Input:**
```json
{}
```
**Expected Output:**
```json
{
  "success": true,
  "build_order": [],
  "error": null
}
```
