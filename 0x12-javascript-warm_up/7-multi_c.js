#!/usr/bin/node

// prints c is fun

const args = process.argv[2];
const a = parseInt(args);
let x = 0;
if (isNaN(a)) {
  console.log('Missing number of occurences');
} while (x < a) {
  console.log('C is fun');
  x++;
}
