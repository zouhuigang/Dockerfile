FROM alpine:edge
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk update
RUN apk upgrade
RUN apk add curl
RUN apk add nginx
RUN apk add php7
RUN apk add php7-dom
RUN apk add php7-ctype
RUN apk add php7-curl
RUN apk add php7-fpm
RUN apk add php7-gd
RUN apk add php7-intl
RUN apk add php7-json
RUN apk add php7-mbstring
RUN apk add php7-mcrypt
RUN apk add php7-mysqlnd
RUN apk add php7-opcache
RUN apk add php7-pdo
RUN apk add php7-pdo_mysql
RUN apk add php7-posix
RUN apk add php7-session
RUN apk add php7-xml
RUN apk add php7-iconv
RUN apk add php7-phar
RUN apk add php7-openssl
RUN apk add tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone
RUN apk del tzdata
RUN rm -rf /var/cache/apk/*
RUN rm -rf /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/nginx.conf
COPY php.ini /etc/php7/conf.d/50-setting.ini
COPY php-fpm.conf /etc/php7/php-fpm.conf
RUN ln -s /usr/bin/php7 /usr/bin/php
ADD run.sh /run.sh
RUN chmod +x /run.sh
EXPOSE 80 443 9000 9001 9002 9003 9004 9005
VOLUME "/app"
WORKDIR "/app"
CMD ["/run.sh"]
