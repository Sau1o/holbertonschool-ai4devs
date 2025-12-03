// Fixed Type error: Used Object.values to create an array before mapping
const users = {
    alice: {name: "Alice", age: 30},
    bob: {name: "Bob", age: 25}
};

function getNames(u) {
    // Fix: Convert object values to array first
    return Object.values(u).map(user => user.name);
}

const names = getNames(users);
console.log(names); // Expected ["Alice", "Bob"]
console.assert(JSON.stringify(names) === JSON.stringify(["Alice", "Bob"]), "Test failed");
