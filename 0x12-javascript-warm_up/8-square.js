#!/usr/bin/node
// a script that prints a square

const a = parseInt(process.argv[2]);
let x = 0;
if (isNaN(a)) {
  console.log('Missing size');
} while (x < a) {
  console.log('X'.repeat(a));
  x++;
}
