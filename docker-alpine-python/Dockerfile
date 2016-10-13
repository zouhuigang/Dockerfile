FROM alpine:3.4
RUN apk update
RUN apk upgrade
RUN apk add python
RUN apk add py-mysqldb
RUN apk add py-yaml
RUN apk add py-redis
RUN apk add tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone
RUN apk del tzdata
