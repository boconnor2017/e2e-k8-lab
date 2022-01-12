FROM centos:7
WORKDIR /usr/local/
COPY python .
RUN sh install-python3.sh
RUN sh install-httpd.sh
RUN sh start.sh
RUN /usr/sbin/httpd
