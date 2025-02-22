#!/bin/sh
python3 ftpserver.py 2121 &
php -S 0.0.0.0:8080 $1
