#!/usr/bin/node
const { argv } = process;
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

function add (a, b) {
  return (a + b);
}
const res = add(num1, num2);
console.log(res);
