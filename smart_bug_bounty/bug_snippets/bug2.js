// Service to update user statuses
const db = require('./mockDatabase');

async function updateAllUsers(userIds) {
    const log = [];

    // Bug: Async/Await misuse inside forEach.
    // .forEach() is synchronous and ignores the Promise returned by the async callback.
    // The function 'updateAllUsers' will finish and return 'log' (which is empty)
    // BEFORE the database updates actually happen.
    userIds.forEach(async (id) => {
        try {
            await db.updateStatus(id, 'active');
            log.push(`User ${id} updated.`);
        } catch (err) {
            log.push(`Failed to update ${id}`);
        }
    });

    return log; 
}
