#!/usr/bin/node
// A class Square that inherits from a Rectangle class

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
