#!/bin/bash

find . -name "*.log" -mtime -1

grep "ERROR" ../logs/application.log
grep -c "ERROR" ../logs/application.log
grep -c "FATAL" ../logs/application.log

grep -c "FATAL" ../logs/system.log
grep -c "CRITICAL" ../logs/system.log
grep "CRITICAL" ../logs/system.log
