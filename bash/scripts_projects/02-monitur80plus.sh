#!/bin/bash

# Monitors disk usage and prints a warning if above 80%

: '
df -h : human readable
grep -w : whole word
tr -d : delete
'



echo "===**- Disk space -**==="
echo "===**- $(df -h | grep -w '/' | awk '{print $5}') -**==="