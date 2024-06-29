const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const router = express.Router();

const dbPath = path.resolve(__dirname, '..', '..', 'detections.db');

const connectDb = () => {
    const db = new sqlite3.Database(dbPath, (err) => {
        if (err) {
            console.error('Could not connect to database', err);
            return;
        }
        console.log('Connected to database');
    });

    return db;
};

const db = connectDb();

router.get('/', (req, res) => {
    let limit = parseInt(req.query.limit) || 20;
    let date = req.query.date || '';

    let query = 'SELECT * FROM detections';
    let params = [];

    if (date) {
        query += ' WHERE DATE(timestamp) = ?';
        params.push(date);
    }

    query += ' ORDER BY timestamp DESC LIMIT ?';
    params.push(limit);

    db.all(query, params, (err, rows) => {
        if (err) {
            return res.status(500).send('Database query error');
        }
        res.render('index', { detections: rows });
    });
});

// Serve images
router.get('/image/:filename', (req, res) => {
    const filepath = path.join(__dirname, '..', '..', 'images', req.params.filename);
    res.sendFile(filepath);
});

module.exports = router;