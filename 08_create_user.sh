#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 username"
    exit 1
fi

USERNAME=$1

if id "$USERNAME" &>/dev/null; then
    echo "User already exists"
else
    sudo useradd -m -G devops "$USERNAME"
    echo "User $USERNAME created and added to devops group"
fi
