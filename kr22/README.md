#!/bin/bash

echo "введите адрес сервера"
read adres
ssh="192.168.122.200"
echo $adres
if [ "$adres" = "$ssh" ]
then 
echo "Запускаем пинг"
echo 
ping -c4 $adres
echo "Достаем файл из архива и подготовливаем к копированию "
gunzip -c ~/gitHun/FORKR.tar.gz
echo "Подключаемся для копирования файла "
rsync  -avzhe ssh FORKR.txt  rab2@192.168.122.200:/tmp
echo "Файл скопирован "
ssh -t rab2@192.168.122.200 ' ls -d /tmp/FORKR.txt  && echo Файл находится в директории'
echo "Удаляем архив  из начальной директории"
rm -с ~/gitHun/FORKR.tar.gz

else echo "Введен неправильный адрес"
fi