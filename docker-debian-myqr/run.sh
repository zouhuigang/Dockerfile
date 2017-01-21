#!/bin/sh
/app/server.py &
tail -f /dev/null
