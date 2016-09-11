FROM alpine:edge
RUN apk update
RUN apk upgrade
RUN apk add mysql
RUN apk add mysql-client
RUN apk add tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone
RUN apk del tzdata
VOLUME ["/var/lib/mysql", "/etc/mysql/conf.d"]
ADD run.sh /run.sh
RUN chmod +x /run.sh
CMD ["/run.sh"]
EXPOSE 3306
