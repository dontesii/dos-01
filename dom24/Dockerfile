FROM ubuntu:18.04

RUN apt-get update 
RUN apt-get install -y software-properties-common
RUN add-apt-repository --yes -u ppa:ansible/ansible
RUN apt-get install -y ansible

RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts
COPY . /etc/ansible/
CMD ansible -m ping all
/