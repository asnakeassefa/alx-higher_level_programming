#!/usr/bin/node

const process = require('process');

let first = 0;
let second = 0;

if (process.argv < 2) {
  console.log(second);
} else {
  process.argv.forEach(element => {
    if (first < element) {
      second = first;
      first = element;
    }
  });
}

console.log(second);
