#!/bin/bash
#ssh  rab2@192.168.122.200  
min=0.70
sre=0.80
max=0.90
spc=$(df -k -BG  | grep "/dev/sda6" |  awk '{print ($2-$3)/100}')    
if (( $(echo "$spc > $min" |bc -l) )); then
echo "Занято больше  "$spc"" | mail -s "Свободного места " roooootac@mail.ru 
if (( $(echo "$spc > $sre" |bc -l) )); then
find . -mount -type f -size +512M -print 2>/dev/null | xargs -r -d '\n' ls -lh | sort -k5,5 -h -r | mail -s "Свободного места " roooootac@mail.ru 
if (( $(echo "$spc > $max" |bc -l) )); then
find var/log -type f -exec du -Sh {} + | sort -rh | head -n 5 | rm -rf {}



fi