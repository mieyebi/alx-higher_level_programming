#!/usr/bin/node
// A rectangle class that defines the rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let a = 0;
    while (a < this.height) {
      console.log('X'.repeat(this.width));
      a++;
    }
  }
};
