#!/usr/bin/node
const { argv } = process;
const num = parseInt(argv[2]);
function factorial (a) {
  if (isNaN(a)) {
    return (1);
  }
  if (a === 1) {
    return (1);
  }
  return (a * factorial(a - 1));
}
const res = factorial(num);
console.log(res);
