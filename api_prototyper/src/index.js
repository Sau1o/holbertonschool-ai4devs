const express = require('express');
const app = express();
const PORT = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// In-memory database for prototyping
let items = [
    { id: 1, name: 'Prototype Item A', status: 'active' },
    { id: 2, name: 'Prototype Item B', status: 'pending' }
];

// Helper to generate IDs
const generateId = () => items.length > 0 ? Math.max(...items.map(i => i.id)) + 1 : 1;

// --- CRUD Operations ---

// 1. GET /items (Read All)
app.get('/items', (req, res) => {
    res.json({ 
        success: true, 
        count: items.length, 
        data: items 
    });
});

// 2. GET /items/:id (Read One)
app.get('/items/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const item = items.find(i => i.id === id);

    if (!item) {
        return res.status(404).json({ success: false, message: 'Item not found' });
    }

    res.json({ success: true, data: item });
});

// 3. POST /items (Create)
app.post('/items', (req, res) => {
    const { name, status } = req.body;

    if (!name) {
        return res.status(400).json({ success: false, message: 'Name is required' });
    }

    const newItem = {
        id: generateId(),
        name,
        status: status || 'new'
    };

    items.push(newItem);
    res.status(201).json({ success: true, message: 'Item created', data: newItem });
});

// 4. PUT /items/:id (Update)
app.put('/items/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const { name, status } = req.body;
    const index = items.findIndex(i => i.id === id);

    if (index === -1) {
        return res.status(404).json({ success: false, message: 'Item not found' });
    }

    // Update fields if provided
    if (name) items[index].name = name;
    if (status) items[index].status = status;

    res.json({ success: true, message: 'Item updated', data: items[index] });
});

// 5. DELETE /items/:id (Delete)
app.delete('/items/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const initialLength = items.length;
    
    items = items.filter(i => i.id !== id);

    if (items.length === initialLength) {
        return res.status(404).json({ success: false, message: 'Item not found' });
    }

    res.json({ success: true, message: 'Item deleted successfully' });
});

// Start Server
app.listen(PORT, () => {
    console.log(`API running on port ${PORT}`);
});
