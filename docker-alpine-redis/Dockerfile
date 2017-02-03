FROM alpine:edge
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk update
RUN apk add --update redis
RUN rm -rf /var/cache/apk/*
VOLUME ["/data"]
ADD run.sh /run.sh
RUN chmod a+x /run.sh
ADD redis.conf /etc/redis.conf
CMD ["/run.sh"]
EXPOSE 6379
