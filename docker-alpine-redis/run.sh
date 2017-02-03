#!/bin/sh
/usr/bin/redis-server /etc/redis.conf
tail -f /dev/null
