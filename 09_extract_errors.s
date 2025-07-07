#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 logfile"
    exit 1
fi

grep -i "error" "$1"
