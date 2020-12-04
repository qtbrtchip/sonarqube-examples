// Or async function
module.exports = () => {
  return {
    verbose: true,
    cacheDirectory: "./.tmp/",
    globals: {
      __DEV__: true
    },
    notify: false,
    rootDir: "./",
    roots: [
      "./"
    ],
    testPathIgnorePatterns: ['/node_modules/'],
    testRegex: "/tests/.*\\.(spec)\\.(js)$",
    setupFiles: []
  };
};