#!/bin/sh
nginx &
php-fpm7 -F
tail -f /dev/null
