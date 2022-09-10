#!/usr/bin/node
// A script function that returns the number of occurences

exports.nbOccurences = function (list, searchElement) {
  let a = 0;
  let b = 0;
  while (list[a] != null) {
    if (list[a] === searchElement) {
      b += 1;
    }
    a++;
  }
  return (b);
};
