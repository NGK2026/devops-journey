#!/bin/bash

echo "analysing log files"
echo "==================="

echo "* List of log files updated in last 24 hours"
find ../logs/. -name "*.log" -mtime -1

echo -e "\n* Number of ERROR logs found in application.log"
grep -c "ERROR" ../logs/application.log

echo -e "\n* Number of FATAL logs found in application.log"
grep -c "FATAL" ../logs/application.log

echo -e "\n* Searching ERROR logs in application.log file..."
grep "ERROR" ../logs/application.log

echo -e "\n* Number of FATAL logs found in system.log"
grep -c "FATAL" ../logs/system.log

echo -e "\n* Number of CRITICAL logs found in system.log"
grep -c "CRITICAL" ../logs/system.log

echo -e "\n* Searching CRITICAL logs in application.log file..."
grep "CRITICAL" ../logs/system.log


: ' 
output:

analysing log files
===================
* List of log files updated in last 24 hours
../logs/./application.log
../logs/./system.log

* Number of ERROR logs found in application.log
6

* Number of FATAL logs found in application.log
2

* Searching ERROR logs in application.log file...
[2025-06-01 08:17:48] [ERROR] Payment gateway timeout after 30s for transaction TX78901234
[2025-06-01 08:25:48] [ERROR] Insufficient disk space for file upload
[2025-06-01 08:41:33] [ERROR] Invalid product code: PRD-404-NOTFOUND
[2025-06-01 08:55:19] [ERROR] Failed to update product #5678 - Database constraint violation
[2025-06-01 09:12:17] [ERROR] Analytics processing failed - Missing data for region EU-WEST
[2025-06-01 09:30:45] [ERROR] Health check failed for service: message-queue

* Number of FATAL logs found in system.log
2

* Number of CRITICAL logs found in system.log
5

* Searching CRITICAL logs in application.log file...
Jun  1 01:20:21 server-prod-01 sshd[23954]: [CRITICAL] Disconnecting: Too many authentication failures for root from 198.51.100.23 port 63122 ssh2 [preauth]
Jun  1 01:45:06 server-prod-01 smartd[1234]: [CRITICAL] Device: /dev/sda [SAT], failed SMART usage Attribute: Reallocated_Sector_Ct.
Jun  1 03:46:01 server-prod-01 smartd[1234]: [CRITICAL] Device: /dev/sdc [SAT], failed SMART usage Attribute: Raw_Read_Error_Rate.
Jun  1 04:40:14 server-prod-01 kernel: [59414.567890] [CRITICAL] Hardware event. This is not a software error.
Jun  1 04:40:15 server-prod-01 kernel: [59415.678901] [CRITICAL] MCE: [Hardware Error]: CPU 0: Machine Check: 0 Bank 6: ee00000000800400
'