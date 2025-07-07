#!/bin/bash
packages=("git" "vim" "curl")

for pkg in "${packages[@]}"
do
    if dpkg -s "$pkg" &>/dev/null; then
        echo "$pkg is already installed"
    else
        echo "Installing $pkg..."
        sudo apt-get install -y "$pkg"
    fi
done
