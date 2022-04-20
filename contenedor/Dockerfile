FROM ubuntu:latest
WORKDIR /usr/src/apuntes
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install sphinx
CMD ["make", "html"]