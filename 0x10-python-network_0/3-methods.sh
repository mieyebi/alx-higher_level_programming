#!/bin/bash
# A script that displays all HTTP methods a server will accept
curl -sI $1 | grep Allow | cut -f2- -d' '
