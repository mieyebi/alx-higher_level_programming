#!/usr/bin/node
// A function that converts number from base10 to another base

exports.converter = function (base) {
  function myConverter (n) {
    return n.toString(base);
  }
  return myConverter;
};
