#!/usr/bin/node

const process = require('process');

// add two number
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));
