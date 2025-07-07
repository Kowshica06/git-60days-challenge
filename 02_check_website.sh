#!/bin/bash

URL="https://www.learnxops.com"

if curl -s --head "$URL" | grep "200 OK" > /dev/null; then
    echo "Website is reachable"
else
    echo "Website is not reachable"
fi
