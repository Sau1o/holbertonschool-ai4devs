// Fixed Library misuse: Swapped callback parameters to (err, data)
const fs = require('fs');

// Note: Create a dummy test.txt file before running this if needed
fs.writeFile('test.txt', 'Hello World', () => {
    fs.readFile('test.txt', 'utf8', (err, data) => { // Fix: err first
      if (err) {
        console.error("Error reading file:", err);
        return;
      }
      console.log("File content:", data);
    });
});
