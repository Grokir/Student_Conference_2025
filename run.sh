#!/bin/sh
sudo docker build -t php_vuln_server .
sudo sudo docker run -it -p 80:8080 php_vuln_server /bin/bash
