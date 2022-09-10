#!/usr/bin/node
// A class Square that inherits from a class Square

const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let a = 0;
      while (a < this.height) {
        console.log('C'.repeat(this.width));
        a++;
      }
    }
  }
};
