#!/usr/bin/node
// A script that imports a dictionary and computes a new dictionary

const dict = require('./101-data').dict;
const newDict = {};

for (const item in dict) {
  if (!(dict[item] in newDict)) newDict[dict[item]] = [];
  newDict[dict[item]].push(item);
}
console.log(newDict);
