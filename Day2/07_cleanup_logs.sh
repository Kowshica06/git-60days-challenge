#!/bin/bash
sudo find /var/log -type f -name "*.log" -mtime +7 -exec rm -f {} \;
echo "Old log files deleted."
