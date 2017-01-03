FROM alpine:edge
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk update
RUN apk upgrade
RUN apk add wget
RUN apk add curl
RUN apk add git
RUN apk add php7
RUN apk add php7-curl
RUN apk add php7-openssl
RUN apk add php7-iconv
RUN apk add php7-json
RUN apk add php7-mbstring
RUN apk add php7-phar
RUN apk add php7-dom
RUN apk add tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone
RUN apk del tzdata
RUN rm -rf /var/cache/apk/*
RUN ln -s /usr/bin/php7 /usr/bin/php
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer
RUN mkdir /app
VOLUME "/app"
WORKDIR "/app"
CMD ["/bin/sh"]
ENTRYPOINT ["/bin/sh", "-c"]
