#!/usr/bin/node

const process = require('process');

let first = 0;
let second = 0;

if (process.argv.length < 2) {
  console.log(second);
} else {
  process.argv.forEach(element => {
    if (first < parseInt(element)) {
      second = first;
      first = element;
    } else if (second < parseInt(element)) {
      second = element;
    }
  });
}

console.log(second);
