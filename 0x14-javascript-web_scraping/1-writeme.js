#!/usr/bin/node
/* A script that writes a string to a file */

const fs = require('fs');
const file = process.argv[2];
const strwrite = process.argv[3];
fs.writeFile(file, strwrite, 'utf-8', (err, data) => {
    if (err) {
        console.log(err);
    }
});
