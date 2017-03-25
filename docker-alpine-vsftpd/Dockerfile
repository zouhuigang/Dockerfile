FROM alpine:edge
RUN apk update
RUN apk add vsftpd
RUN apk add db-utils
RUN apk add lftp
RUN mkdir -p /etc/vsftpd
COPY vsftpd.conf /etc/vsftpd/vsftpd.conf
RUN touch /etc/vsftpd/vsftpd.chroot_list
COPY run.sh /run.sh
RUN chmod a+x /run.sh
VOLUME /etc/vsftpd
EXPOSE 21
CMD ["/run.sh"]
