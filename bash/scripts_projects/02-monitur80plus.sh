#!/bin/bash

# Monitors disk usage and prints a warning if above 80%

: '
df -h : human readable
grep -w : whole word
tr -d : delete
'

echo "===**- Disk space -**==="
echo "===**-    $(df -h | grep -w '/' | awk '{print $5}')     -**==="

if [ "$(df -h | grep -w '/' | awk '{print $5}' | tr -d '%')" -gt 80 ]; then
    echo -e "\n ⚠️ ⚠️ ⚠️ WARNING, DISK OVER 80% FULL ⚠️ ⚠️ ⚠️"
fi