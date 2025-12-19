/**
 * Async Data Aggregator
 * Intended: Fetch details for a list of IDs sequentially or concurrently 
 * and return the complete list of details.
 */

const fetch = require('node-fetch'); // Mock import

async function getDetails(ids) {
    const results = [];

    // Bug: Array.forEach does not await async callbacks.
    // The function will return 'results' (empty) immediately, 
    // while the fetch operations run in the background detached.
    ids.forEach(async (id) => {
        try {
            const data = await fetch(`https://api.mock.com/items/${id}`);
            const json = await data.json();
            results.push(json);
        } catch (e) {
            console.error(e);
        }
    });

    return results; // Returns [] immediately
}

// Usage
getDetails([1, 2, 3]).then(console.log);
