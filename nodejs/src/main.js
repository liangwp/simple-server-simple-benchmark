'use-strict';

const express = require('express');

var app = express();

app.get('/', (req, res, next) => {
    // a cpu-bound loop
    let counter = 0;
    let counter_max = 100_000;
    while (counter < counter_max) {
        counter += 1;
    }
    res.json({
        hello: 'world'
    });
});

app.listen(8000, () => {
    console.log(`Server listening on port 8000`);
});
