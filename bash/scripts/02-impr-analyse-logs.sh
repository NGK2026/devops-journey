#!/bin/bash

echo "analysing log files"
echo "==================="

echo "* List of log files updated in last 24 hours"
find ../logs/. -name "*.log" -mtime -1
echo

echo "* Number of ERROR logs found in application.log"
grep -c "ERROR" ../logs/application.log
echo

echo "* Number of FATAL logs found in application.log"
grep -c "FATAL" ../logs/application.log
echo

echo "* Searching ERROR logs in application.log file..."
grep "ERROR" ../logs/application.log
echo

echo "* Number of FATAL logs found in system.log"
grep -c "FATAL" ../logs/system.log
echo

echo "* Number of CRITICAL logs found in system.log"
grep -c "CRITICAL" ../logs/system.log
echo

echo "* Searching CRITICAL logs in application.log file..."
grep "CRITICAL" ../logs/system.log
echo
