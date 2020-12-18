# 1. Поднять любой контейнер, положить туда файлы и сделать образ. Закинут *образ на докерах*
```dockerfile
FROM ubuntu
MAINTAINER Dontesi
RUN apt-get update
```
```bash
ending build context to Docker daemon  431.6kB
Step 1/3 : FROM ubuntu
 ---> f643c72bc252
Step 2/3 : MAINTAINER Dontesi
 ---> Using cache
 ---> 716c90d088c0
Step 3/3 : RUN apt-get update
 ---> Using cache
 ---> 1e5fe915f15a
Successfully built 1e5fe915f15a
Successfully tagged dockerfile:latest
```
и + ко всему добавим файл в сам контейнер 
 sudo docker cp 1.txt 06e1803e0b13:/1.txt
```bash
gitHun> sudo docker push dockerfile
Using default tag: latest
The push refers to repository [docker.io/library/dockerfile]
cccbe2eaf3cf: Preparing 
f6253634dc78: Preparing 
9069f84dbbe9: Preparing 
bacd3af13903: Preparing 
```

# 2. Один ли слой будет при run apt-get на разных строках

Будут на разных слоях если прописать как указано  на примере ниже,а если через &&  и на одно строке то один слой.
RUN apt-get update
RUN apt-get install 


