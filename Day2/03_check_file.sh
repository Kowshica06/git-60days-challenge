#!/bin/bash

# Check if a filename argument is given
if [ $# -eq 0 ]; then
    echo "Usage: $0 filename"
    exit 1
fi

FILE="$1"

# Check if the file exists
if [ -f "$FILE" ]; then
    echo "File exists. Contents:"
    cat "$FILE"
else
    echo "File does not exist"
fi
