const runMe = require('../../shared/run-me-lib');

test('Run me', () => {
  // without exception
  // runMe.runMe({rate: 1000});
  // with exception
  runMe.runMe();

  runMe.printMe(1);
  runMe.printMe(2);
});