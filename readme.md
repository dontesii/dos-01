
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
ansible_ssh_user=root
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

useradd vagrant
passwd vagrant
Повысить привилегии пользователя в системе для использования sudo:

usermod -aG wheel vagrant
Обновить систему:
yum update -y
Настройка sudoers
Отредактировать sudoers файл: 

nano /etc/sudoers
Добавить, изменить некоторые параметры к текущему виду, изменить параметр Defaults !requiretty на:

Defaults   !requiretty
 Добавить к:

Defaults    env_keep += "LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE"
Defaults    env_keep += "LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY"
 Параметр:

Defaults    env_keep += "SSH_AUTH_SOCK"
 Изменить параметры группы wheel:

%wheel  ALL=(ALL) NOPASSWD: ALL
Настройка sshd
Открыть файл:

/etc/ssh/sshd_config
Изменить параметр AuthorizedKeysFile на:

AuthorizedKeysFile  %h/.ssh/authorized_keys
 Раскомментировать и выставить No у параметра UseDNS:

UseDNS no
 Перезапустить sshd:

systemctl restart sshd.service
Установка vagrant ssh ключей
После загрузки машины, войти под учетной записью vagrant, создать каталог:

mkdir .ssh && chmod 0700 .ssh/ && cd .ssh
Загрузить vagrant ключ с офф репозитория:

wget --no-check-certificate https://raw.githubusercontent.com/hashicorp/vagrant/master/keys/vagrant.pub -O authorized_keys
Задать правильные разрешения:

chmod 0600 authorized_keys

Подключить образ в меню VirtualBox - Devices - Insert Guest Additions CD image... Далее необходимо создать папку монтирования, примонтировать в нее cdrom:

sudo mkdir /mnt/cdrom && sudo mount /dev/cdrom /mnt/cdrom && cd /mnt/cdrom
 Убедиться, что в данном каталоге есть файлы (можно использовать команду ls), запустить установку VirtualBox дополнений:

sudo ./VBoxLinuxAdditions.run
 После установки отмонтировать cdrom:

sudo umount /mnt/cdrom

jerson:~/ansible$ cd
jerson:~$ mkdir vagrant-box && cd vagrant-box
jerson:~/vagrant-box$ vagrant box list

jerson:~/vagrant-box$ vagrant package --base Cent
==> Cent: Exporting VM...
==> Cent: Compressing package to: /home/jersonvagrant-box/package.box

==> box: Box file was not detected as metadata. Adding it directly...
==> box: Adding box 'centos8-custom' (v0) for provider: 
    box: Unpacking necessary files from: file:///home/jerson/vagrant-box/package.box
==> box: Successfully added box 'centos8-custom' (v0) for 'virtualbox'!
jerson:~/vagrant-box$ vagrant box list
centos8-custom (virtualbox, 0)
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
1

## 1.Пользователь вводит строку из букв в нижнем регистре. Нужно посчитать, сколько в этой строке английских гласных букв. Корректность ввода не проверять.


a = input('Введи строку : ')
glas = 'aeyuoi'
b = []
for i in a:
    if i in glas:
        b.append(i)
print('гласных :',len(b))


## 2.Клиент покупает кофе в кафе. За каждые 6 чашек, 1 чашка даётся в качестве бонуса.Задача: запросить у пользователя кол-во чашек на покупку, вычислить полагающееся кол-во бонусных чашек кофе и вывести это число на консоль.В функцию можно передать строку, которая будет выведена на экран для общения с пользователем, например:
age = input('Введите ваш возраст')

a = int(input("Введите коль-во чашек кофе : "))
b=(a//6)
print("Количество бонусных чашек:", b )

## 3.Запросить у пользователя координаты x и y двух точек на плоскости. Посчитать расстояние между заданными точками и вывести результат на консоль с точностью до трёх знаков после запятой (плавающей точки).Примечание: у каждой точки есть две координаты: x и y. Формулу в интернете можно посмотреть.


import math
x1=int(input("Введите x1 : "))
y1=int(input("Введите y1 : "))
x2=int(input("Введите x2 : "))
y2=int(input("Введите y2 : "))

from math import sqrt
dist = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))



print("Расстояние между точками:", dist )

