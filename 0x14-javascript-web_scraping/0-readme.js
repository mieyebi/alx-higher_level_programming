#!/usr/bin/node
/* A Script that reads and prints the content of a file */

const fs = require('fs');
const file = processs.argv[2];
js.readFile(file, 'utf8', (err, data) => {
    if (err) {
        console.log(err);
    } else {
        console.log(data);
    }
});
