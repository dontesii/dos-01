#!/bin/bash 
echo "Тип ОС:  $OSTYPE" 
echo "Имя ОС: $HOSTNAME "
echo "Верися Ядра: " 
uname -a | awk ' {print $3} ' 
echo "Ip адрес:" 
ip r l | grep wlp1s0
echo "LA за последние 15 минут"
cat /proc/loadavg | awk ' {print $3} '
echo "Время работы системы: "
uptime | awk ' {print $2, $3, $4, $5} '
echo "Информация об использованной RAM: "
cat /proc/meminfo | grep Mem
echo "Информацию об авторизованных пользователях:"
w -s
