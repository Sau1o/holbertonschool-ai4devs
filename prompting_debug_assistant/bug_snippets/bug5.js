// Misuse of data types / libraries: intended to map over an array of user objects and return names
const users = {
    alice: {name: "Alice", age: 30},
    bob: {name: "Bob", age: 25}
};

function getNames(u) {
    // BUG: users is an object, not an array. Using map will throw: users.map is not a function
    return Object.keys(u).map(user => u[user].name);
}

console.log(getNames(users)); // expected ["Alice","Bob"]
