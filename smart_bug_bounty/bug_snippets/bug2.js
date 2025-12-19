/**
 * User Data Fetcher Service
 * Fetches user profiles from a mock API.
 */

const fetch = require('node-fetch'); // Hypothetical import

async function getUserIds() {
    return [101, 102, 103, 104];
}

async function fetchUserProfile(id) {
    // Simulating API call
    return new Promise(resolve => setTimeout(() => resolve({ id, name: `User${id}` }), 100));
}

async function getAllProfiles() {
    const ids = await getUserIds();
    const profiles = [];

    // BUG: forEach expects a synchronous function. 
    // The async callback here will just fire off promises that aren't awaited by forEach.
    // 'profiles' will be returned empty before the callbacks complete.
    ids.forEach(async (id) => {
        try {
            const profile = await fetchUserProfile(id);
            profiles.push(profile);
            console.log(`Fetched ${profile.name}`);
        } catch (error) {
            console.error("Error fetching user", id);
        }
    });

    console.log("Finished fetching profiles.");
    return profiles; 
}

// Execution
getAllProfiles().then(data => console.log("Final List:", data));
