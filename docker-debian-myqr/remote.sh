#!/bin/sh
echo 'please select:'
echo '1.docker images -a'
echo '2.docker ps -a'
echo '3.docker rm -f @container'
echo '4.docker rmi -f @image'
echo '5.docker pull @image'
echo '6.docker-compose up -d'
echo '7.docker exec -it @container sh'
image=hub.docker8.net/web/myqr
container=myqr
count=$#
if [ $count -gt 0 ]
    then
        name=$1
else
    read name
fi
case $name in
    '1')
        sudo docker images -a
        ;;
    '2')
        sudo docker ps -a
        ;;
    '3')
        sudo docker rm -f $container
        ;;
    '4')
        sudo docker rmi -f $image
        ;;
    '5')
        sudo docker pull $image
        ;;
    '6')
        sudo docker-compose --file=/data/service/myqr/docker-compose.yml up -d
        ;;
    '7')
        sudo docker exec -it $container sh
        ;;
    *)
        echo "not find"
        ;;
    esac
