#!/bin/sh
adduser -h ${FTP_HOME} -s /bin/false -D ${FTP_SUPER_USER}
adduser -h ${FTP_HOME} -s /bin/false -D ${FTP_USER}
echo "${FTP_SUPER_USER}:$(echo ${FTP_SUPER_PASSWORD} | mkpasswd -m SHA-512)" | chpasswd -e
echo "${FTP_USER}:$(echo ${FTP_PASSWORD} | mkpasswd -m SHA-512)" | chpasswd -e
chmod a-w ${FTP_HOME}
mkdir -p ${FTP_HOME}/${FTP_DATA_DIR}
chmod 777 ${FTP_HOME}/${FTP_DATA_DIR}
killall vsftpd
/usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf &
if [ -e /runAndInit.sh ];then /runAndInit.sh;fi
tail -f /dev/null
