#!/usr/bin/node
const process = require('process');

if (parseInt(process.argv[2])) {
  for (let x = 0; x < parseInt(process.argv[2]); x++) {
    for (let y = 0; y < parseInt(process.argv[2]); y++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
