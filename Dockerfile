FROM php:8.2-cli
RUN apt-get update
RUN apt-get install -y vim iproute2 python3 python3-twisted
WORKDIR /var/www/php-app
# ADD vuln_app .
ADD sec_app .
RUN chmod +x run.sh
RUN mkdir /var/log/pyftp/
RUN mv root.txt /root
RUN echo "Directory_traversal_FLAG=7616c666f5c61637275667162747f5279646f5078607" >> /etc/passwd
ENTRYPOINT ["./run.sh"]

