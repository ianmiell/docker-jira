FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y -qq curl git python-pip
WORKDIR /opt
RUN git clone https://github.com/ianmiell/shutit.git
WORKDIR shutit
RUN pip install -r requirements.txt

WORKDIR /space/git/docker-jira2 <- TODO You will likely need to to change this
RUN /opt/shutit/shutit build --shutit_module_path /opt/shutit/library --delivery bash

CMD ["/bin/bash"] 