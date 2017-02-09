FROM alpine:edge
RUN apk update
RUN apk add nodejs
RUN npm install -g react-tools
RUN rm -rf /var/cache/apk/*
ENTRYPOINT jsx --watch /tmp/from /tmp/to
