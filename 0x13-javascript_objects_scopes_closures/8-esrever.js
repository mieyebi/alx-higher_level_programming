#!/usr/bin/node
// A function that returns the reversed version of a list

exports.esrever = function (list) {
  let a = list.length - 1;
  const revlist = [];
  while (a >= 0) {
    revlist.push(list[a]);
    a--;
  }
  return (revlist);
};
