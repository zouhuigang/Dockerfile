FROM debian:latest
RUN apt-get update
RUN apt-get install -y python3-dev
COPY get-pip.py /tmp/get-pip.py
RUN chmod a+x /tmp/get-pip.py
RUN python3 /tmp/get-pip.py
RUN pip install myqr
RUN pip install bottle
RUN rm -rf /tmp/get-pip.py
RUN mkdir -p /app/temp
COPY run.sh /app/run.sh
RUN chmod a+x /app/run.sh
COPY server.py /app/server.py
RUN chmod a+x /app/server.py
WORKDIR /app
EXPOSE 80 443 50001
CMD ["/app/run.sh"]
