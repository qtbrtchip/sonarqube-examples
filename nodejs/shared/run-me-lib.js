module.exports = {
  runMe(config) {
    let count
    try {
      count = 100 / config.rate
    } catch (error) {
      count = 0
      console.log('some error', error);
    }

    console.log('count', count);
  },

  printMe(userId) {
    if (userId == 1) {
      console.log('Hello, David');
    } else {
      console.log('Hello, John');
    }
  }
}