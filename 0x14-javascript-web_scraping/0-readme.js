#!/usr/bin/node
//The first argument is the file path

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
