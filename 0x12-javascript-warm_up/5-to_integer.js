#!/usr/bin/node
// a script that converts arguments to integers

const args = process.argv;
const a = parseInt(args[2]);
if (isNaN(a)) {
  console.log('Not a number');
} else {
  console.log('My number: 'a);
}
