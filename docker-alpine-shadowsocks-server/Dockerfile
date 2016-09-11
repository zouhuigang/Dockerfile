FROM alpine:3.4
RUN apk update
RUN apk upgrade
RUN apk add python
RUN apk add py-pip
RUN apk add tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone
RUN apk del tzdata
RUN pip install shadowsocks
ENV SERVER_IP 0.0.0.0
ENV SERVER_PORT 1080
ENV SERVER_PASSWORD 1234
ENV SERVER_METHOD aes-256-cfb
ENV SERVER_TIMEOUT 300
EXPOSE $SERVER_PORT
ENTRYPOINT ssserver -s $SERVER_IP -p $SERVER_PORT -k $SERVER_PASSWORD -m $SERVER_METHOD -t $SERVER_TIMEOUT
