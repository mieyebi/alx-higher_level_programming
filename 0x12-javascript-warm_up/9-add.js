#!/usr/bin/node
// Prints the addition of 2 integers

const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);
function add (a, b) {
  console.log(a + b);
}
add(a, b);
