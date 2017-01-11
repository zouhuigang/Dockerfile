#!/bin/sh
nginx &
php-fpm7
sleep 10
if [ -e /runAndInit.sh ];then /runAndInit.sh;fi
tail -f /dev/null
