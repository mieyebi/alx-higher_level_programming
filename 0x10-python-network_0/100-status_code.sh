#!/bin/bash
# A script that outputs the status code of an HTTP response
curl $1 -sI -w '%{http_code}' -o /dev/null
