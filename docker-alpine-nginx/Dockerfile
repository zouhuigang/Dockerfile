FROM alpine:latest
ENV TIMEZONE Asia/Shanghai
RUN	apk update && \
	apk upgrade && \
	apk add --update openssl nginx && \
	apk add --update tzdata && \
	cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
	echo "${TIMEZONE}" > /etc/timezone && \
	apk del tzdata && \
	rm -rf /var/cache/apk/*
ADD nginx.conf /etc/nginx/nginx.conf
VOLUME ["/etc/nginx/conf.d"]
EXPOSE 80 443
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]
