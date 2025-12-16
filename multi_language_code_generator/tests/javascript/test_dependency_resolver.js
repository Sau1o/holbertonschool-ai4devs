const assert = require('assert');
const DependencyResolver = require('../../implementations/javascript/dependencyResolver');

const resolver = new DependencyResolver();
console.log("Running Tests...");

// Test 1: Simple Chain
try {
    const data = { "A": ["B"], "B": ["C"], "C": [] };
    const result = resolver.resolve(data);
    assert.strictEqual(result.success, true);
    assert.deepStrictEqual(result.build_order, ["C", "B", "A"]);
    console.log("✓ Test 1 Passed");
} catch (e) { console.error("✗ Test 1 Failed", e); }

// Test 2: Diamond Dependency
try {
    const data = { "App": ["Lib1", "Lib2"], "Lib1": ["Core"], "Lib2": ["Core"], "Core": [] };
    const result = resolver.resolve(data);
    assert.strictEqual(result.success, true);
    const order = result.build_order;
    assert.strictEqual(order[0], "Core");
    assert.strictEqual(order[order.length - 1], "App");
    // Lib1 and Lib2 must be present in the middle
    const middle = order.slice(1, 3).sort();
    assert.deepStrictEqual(middle, ["Lib1", "Lib2"]);
    console.log("✓ Test 2 Passed");
} catch (e) { console.error("✗ Test 2 Failed", e); }

// Test 3: Circular Direct
try {
    const data = { "A": ["B"], "B": ["A"] };
    const result = resolver.resolve(data);
    assert.strictEqual(result.success, false);
    assert.ok(result.error);
    console.log("✓ Test 3 Passed");
} catch (e) { console.error("✗ Test 3 Failed", e); }

// Test 4: Circular Indirect
try {
    const data = { "A": ["B"], "B": ["C"], "C": ["A"] };
    const result = resolver.resolve(data);
    assert.strictEqual(result.success, false);
    console.log("✓ Test 4 Passed");
} catch (e) { console.error("✗ Test 4 Failed", e); }

// Test 5: Disconnected Graphs
try {
    const data = { "Front": ["UI"], "UI": [], "Back": ["DB"], "DB": [] };
    const result = resolver.resolve(data);
    assert.strictEqual(result.success, true);
    const order = result.build_order;
    assert.ok(order.indexOf("UI") < order.indexOf("Front"));
    assert.ok(order.indexOf("DB") < order.indexOf("Back"));
    console.log("✓ Test 5 Passed");
} catch (e) { console.error("✗ Test 5 Failed", e); }

// Test 6: Empty Input
try {
    const data = {};
    const result = resolver.resolve(data);
    assert.strictEqual(result.success, true);
    assert.deepStrictEqual(result.build_order, []);
    console.log("✓ Test 6 Passed");
} catch (e) { console.error("✗ Test 6 Failed", e); }

// Test 7: Self Dependency
try {
    const data = { "A": ["A"] };
    const result = resolver.resolve(data);
    assert.strictEqual(result.success, false);
    console.log("✓ Test 7 Passed");
} catch (e) { console.error("✗ Test 7 Failed", e); }

// Test 8: Redundant Dependencies
try {
    const data = { "A": ["B", "B"], "B": [] };
    const result = resolver.resolve(data);
    assert.strictEqual(result.success, true);
    assert.deepStrictEqual(result.build_order, ["B", "A"]);
    console.log("✓ Test 8 Passed");
} catch (e) { console.error("✗ Test 8 Failed", e); }

// Test 9: Implicit Dependency
try {
    const data = { "App": ["Utils"] };
    const result = resolver.resolve(data);
    assert.strictEqual(result.success, true);
    assert.deepStrictEqual(result.build_order, ["Utils", "App"]);
    console.log("✓ Test 9 Passed");
} catch (e) { console.error("✗ Test 9 Failed", e); }

// Test 10: Complex Structure
try {
    const data = {
        "Dashboard": ["Widget", "Auth"],
        "Widget": ["Charts", "Styles"],
        "Charts": ["D3"],
        "Auth": ["Styles", "DB"],
        "Styles": [], "DB": [], "D3": []
    };
    const result = resolver.resolve(data);
    assert.strictEqual(result.success, true);
    const order = result.build_order;
    assert.ok(order.indexOf("D3") < order.indexOf("Charts"));
    assert.ok(order.indexOf("Styles") < order.indexOf("Widget"));
    assert.ok(order.indexOf("Widget") < order.indexOf("Dashboard"));
    console.log("✓ Test 10 Passed");
} catch (e) { console.error("✗ Test 10 Failed", e); }
