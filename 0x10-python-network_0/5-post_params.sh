#!/bin/bash
# A script that sends a POST request using curl
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
