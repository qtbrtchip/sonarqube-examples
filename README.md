## Fix issue when running Elastic Search

Update max_map_count
- sudo sysctl -w vm.max_map_count=262144
- edit /etc/sysctl.conf, then add/update vm.max_map_count=262144
- restart docker: `systemctl restart docker`

## Run sonarqube locally
- docker-compose up
- open sonarqube on browser: 'http://localhost:9000/
- login with account: admin/admin
