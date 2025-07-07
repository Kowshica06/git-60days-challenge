#!/bin/bash

while true
do
    echo "Time: $(date)" >> system_usage.log
    echo "CPU Load: $(uptime | awk -F'load average:' '{ print $2 }')" >> system_usage.log
    echo "Memory Usage: $(free -m | awk '/Mem:/ { print "Used: "$3"MB, Free: "$4"MB" }')" >> system_usage.log
    echo "---" >> system_usage.log
    sleep 5
done
