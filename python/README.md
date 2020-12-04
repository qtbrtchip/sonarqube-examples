
## Generate report for code coverage
pytest --cov-report xml:coverage-reports/pytest-coverage-report.xml --cov-report annotate --cov=. tests/
or
pytest --cov-report html --cov-report xml:coverage-reports/pytest-coverage-report.xml --cov-report annotate --cov=. tests/

## Run sonarqube
- for current project: http://localhost:9000/dashboard?id=simple-py-project
sonar-scanner   -Dsonar.projectKey=simple-py-project   -Dsonar.sources=.   -Dsonar.host.url=http://localhost:9000   -Dsonar.login=833f073f89f795d1d0c0e25c1126450c9d628cf7

## sonarqube notes
- We should exclude htmlcov which is generated my pytest-cov:

