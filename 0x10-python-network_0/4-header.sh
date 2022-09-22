#!/bin/bash
# A script that srnds a GET request with custom set HEADER variable
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
