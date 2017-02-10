FROM alpine:edge
RUN apk update
RUN apk add nodejs
RUN npm install -g babel-cli
RUN mkdir -p /tmp/babel/from
RUN mkdir -p /tmp/babel/to
RUN cd /tmp/babel
RUN npm install --save-dev babel-cli
RUN npm install --save-dev babel-core
RUN npm install --save-dev babel-preset-es2015
RUN npm install --save-dev babel-preset-react
COPY babelrc /tmp/babel/.babelrc
COPY package.json /tmp/babel/package.json
COPY crontab /etc/crontabs/root
COPY run.sh /tmp/run.sh
COPY crontab.sh /tmp/crontab.sh
RUN chmod a+x /tmp/run.sh /tmp/crontab.sh
VOLUME "/tmp/babel/from"
VOLUME "/tmp/babel/to"
WORKDIR "/tmp/babel"
CMD ["/tmp/run.sh"]
RUN rm -rf /var/cache/apk/*

