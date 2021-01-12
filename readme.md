# 1.Развернуть систему управления конфигруацией ansible в докере и управлять нашими хостами
```
FROM ubuntu:18.04

RUN apt-get update 
RUN apt-get install -y software-properties-common
RUN add-apt-repository --yes -u ppa:ansible/ansible
RUN apt-get install -y ansible

RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts
COPY . /etc/ansible/
CMD ansible -m ping all
```



# 2.Развернуть 4 виртуальные машины ubuntu и создать inventory file (db и app для дев и prod). Выполнить пинг через ansible для группы дев и прод.
Так как мощностей не хватает я развернул только 2.
```
[dev]
centos1 ansible_ssh_host=192.168.122.239

[prod]
ubuntu1 ansible_ssh_host=192.168.122.186 

[dev:vars] 
ansible_ssh_user=root
ansible_ssh_private_key_file=~/.ssh/id_rsa

[prod:vars]
ansible_ssh_user=rab2
ansible_ssh_private_key_file=~/.ssh/id_rsa

Пингуем 

dom24> ansible all -m ping
centos1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/libexec/platform-python"
    },
    "changed": false,
    "ping": "pong"
}
centos2 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/libexec/platform-python"
    },
    "changed": false,
    "ping": "pong"
}
dom24> 
```


# 3.Подготовить шаблон для развертывания centos
Шаблон будет докинут доп.файлом.
# 4.Повторить пункт 2 только в докере.
```
FROM ubuntu:18.04

RUN apt-get update && \
apt-get install -y software-properties-common &&\
add-apt-repository --yes -u ppa:ansible/ansible &&\
apt-get install -y ansible

RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts
COPY . /etc/ansible/
CMD ansible -m ping all

file hosts

[dev]
centos1 ansible_ssh_host=192.168.122.239

[prod]
centos2 ansible_ssh_host=192.168.122.186 

[dev:vars]
ansible_ssh_user=root 

[prod:vars]
ansible_ssh_user=root


[defaults]
inventory = ./hosts.txt
host_key_checking = false 
ost_key_auto_add = True

Пингуем 

}
centos1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/platform-python"
    }, 
    "changed": false, 
    "ping": "pong"
}
centos2 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/platform-python"
    }, 
    "changed": false, 
    "ping": "pong"
}
```