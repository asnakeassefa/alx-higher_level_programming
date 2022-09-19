#!/usr/bin/node

const process = require('process');

if (parseInt(process.argv[2])) {
  for (let v = 0; v < parseInt(process.argv[2]); v++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
