## token
3c792759fe202c19350e44e4fb43692adb2736f7

## Generate code coverage
npm test -- --coverage

## Run sonar scanner
sonar-scanner \
  -Dsonar.projectKey=simple-nodejs-project \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=3c792759fe202c19350e44e4fb43692adb2736f7

