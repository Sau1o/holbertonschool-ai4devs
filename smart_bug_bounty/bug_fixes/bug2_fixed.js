/**
 * FIX APPLIED:
 * Replaced .forEach() with a for...of loop to properly await asynchronous operations.
 */
const db = require('./mockDatabase');

async function updateAllUsers(userIds) {
    const log = [];

    // Fix: usage of for...of allows awaiting inside the loop
    for (const id of userIds) {
        try {
            await db.updateStatus(id, 'active');
            log.push(`User ${id} updated.`);
        } catch (err) {
            log.push(`Failed to update ${id}`);
        }
    }

    return log; 
}
