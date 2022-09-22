#!/bin/bash
# A bash script that takes in a URL and sends a request displaying the bodysize
curl -w '%{size_download}\n' -so /dev/null $1
