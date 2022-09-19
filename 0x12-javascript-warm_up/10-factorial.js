#!/usr/bin/node

const process = require('process');

function factorial (f) {
  let factor = 1;
  for (let x = parseInt(f); x >= 1; x--) {
    factor = factor * x;
  }
  return factor;
}

console.log(factorial(process.argv[2]));
