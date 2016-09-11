#!/bin/sh
chown mysql:mysql /var/lib/mysql -R && /usr/bin/mysql_install_db --user=mysql --datadir=/var/lib/mysql && /usr/bin/mysqld_safe &
sleep 10
/usr/bin/mysqladmin -u root password $MYSQL_PASSWORD
tail -f /dev/null
