#!/usr/bin/node
// A function that executes x times a function

exports.callMeMoby = function (x, theFunction) {
  let a = 0;
  while (a < x) {
  theFunction ();
  a++;
  }
};
