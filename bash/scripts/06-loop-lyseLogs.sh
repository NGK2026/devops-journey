#!/bin/bash

# use variables for repeated values
LOG_DIR="/home/student/projects/git/devops-journey/bash/logs"

# array variable
ERROR_PATTERNS=("ERROR" "FATAL" "CRITICAL")

echo "analysing log files"
echo "==================="

echo "* List of log files updated in last 24 hours"
# command substitution
LOG_FILES=$(find $LOG_DIR -name "*.log" -mtime -1)
echo $LOG_FILES

# loop
for LOG_FILE in $LOG_FILES; do

    echo -e "\n* Searching ${ERROR_PATTERNS[0]} logs in $LOG_FILE file..."
    grep "${ERROR_PATTERNS[0]}" "$LOG_FILE"

    echo -e "\n* Searching ${ERROR_PATTERNS[2]} logs in $LOG_FILE file..."
    grep "${ERROR_PATTERNS[2]}" "$LOG_FILE"

    echo -e "\n* Number of ${ERROR_PATTERNS[0]} logs found in $LOG_FILE"
    grep -c "${ERROR_PATTERNS[0]}" "$LOG_FILE"

    echo -e "\n* Number of ${ERROR_PATTERNS[1]} logs found in $LOG_FILE"
    grep -c "${ERROR_PATTERNS[1]}" "$LOG_FILE"

    echo -e "\n* Number of ${ERROR_PATTERNS[2]} logs found in $LOG_FILE"
    grep -c "${ERROR_PATTERNS[2]}" "$LOG_FILE"



done

: ' 
output:

analysing log files
===================
* List of log files updated in last 24 hours
/home/student/projects/git/devops-journey/bash/logs/application.log /home/student/projects/git/devops-journey/bash/logs/system.log

* Searching ERROR logs in /home/student/projects/git/devops-journey/bash/logs/application.log file...
[2025-06-01 08:17:48] [ERROR] Payment gateway timeout after 30s for transaction TX78901234
[2025-06-01 08:25:48] [ERROR] Insufficient disk space for file upload
[2025-06-01 08:41:33] [ERROR] Invalid product code: PRD-404-NOTFOUND
[2025-06-01 08:55:19] [ERROR] Failed to update product #5678 - Database constraint violation
[2025-06-01 09:12:17] [ERROR] Analytics processing failed - Missing data for region EU-WEST
[2025-06-01 09:30:45] [ERROR] Health check failed for service: message-queue

* Searching CRITICAL logs in /home/student/projects/git/devops-journey/bash/logs/application.log file...
[2025-06-01 08:32:13] [CRITICAL] Database connection lost during backup
[2025-06-01 09:17:22] [CRITICAL] Security alert: Multiple failed login attempts for admin account

* Number of ERROR logs found in /home/student/projects/git/devops-journey/bash/logs/application.log
6

* Number of FATAL logs found in /home/student/projects/git/devops-journey/bash/logs/application.log
2

* Number of CRITICAL logs found in /home/student/projects/git/devops-journey/bash/logs/application.log
2

* Searching ERROR logs in /home/student/projects/git/devops-journey/bash/logs/system.log file...
Jun  1 01:20:18 server-prod-01 sshd[23954]: [ERROR] Failed password for root from 198.51.100.23 port 63122 ssh2
Jun  1 01:20:19 server-prod-01 sshd[23954]: [ERROR] Failed password for root from 198.51.100.23 port 63122 ssh2
Jun  1 01:20:20 server-prod-01 sshd[23954]: [ERROR] Failed password for root from 198.51.100.23 port 63122 ssh2
Jun  1 01:45:03 server-prod-01 kernel: [49413.345678] [ERROR] JBD2: Detected IO errors while flushing file data on sda1-8
Jun  1 01:45:04 server-prod-01 kernel: [49414.456789] [ERROR] Buffer I/O error on device sda1, logical block 12345678
Jun  1 01:50:24 server-prod-01 kernel: [49734.109876] [ERROR] XFS (sdb1): Please unmount the filesystem and rectify the problem(s)
Jun  1 02:15:15 server-prod-01 systemd[1]: [ERROR] Failed to start Daily apt upgrade and clean activities.
Jun  1 03:45:23 server-prod-01 mdadm[25134]: [ERROR] RebuildFinished event detected on md device /dev/md0, but rebuild failed
Jun  1 03:45:25 server-prod-01 kernel: [56725.567890] md/raid1:md0: [ERROR] sdc1: rescheduling sector 7654321 for read
Jun  1 03:45:26 server-prod-01 kernel: [56726.678901] md/raid1:md0: [ERROR] sdc1: read error at offset 7654321 on device sdc1
Jun  1 04:40:12 server-prod-01 kernel: [59412.345678] [ERROR] Memory failure: 0x00000000aa2b5000: recovery action unavailable
Jun  1 04:40:13 server-prod-01 kernel: [59413.456789] [ERROR] EDAC MC0: 1 CE memory read error on CPU_SrcID#0_MC#0_Chan#0_DIMM#0 (channel:0 slot:0 page:0x0 offset:0x0 grain:8 syndrome:0x0 - area:DRAM err_code:0001:0091 socket:0 channel_mask:1)
Jun  1 04:40:16 server-prod-01 kernel: [59416.789012] [ERROR] EDAC MC0: 1 CE memory read error on CPU_SrcID#0_MC#0_Chan#0_DIMM#0 (channel:0 slot:0 page:0x0 offset:0x0 grain:8 syndrome:0x0 - area:DRAM err_code:0001:0091 socket:0 channel_mask:1)

* Searching CRITICAL logs in /home/student/projects/git/devops-journey/bash/logs/system.log file...
Jun  1 01:20:21 server-prod-01 sshd[23954]: [CRITICAL] Disconnecting: Too many authentication failures for root from 198.51.100.23 port 63122 ssh2 [preauth]
Jun  1 01:45:06 server-prod-01 smartd[1234]: [CRITICAL] Device: /dev/sda [SAT], failed SMART usage Attribute: Reallocated_Sector_Ct.
Jun  1 03:46:01 server-prod-01 smartd[1234]: [CRITICAL] Device: /dev/sdc [SAT], failed SMART usage Attribute: Raw_Read_Error_Rate.
Jun  1 04:40:14 server-prod-01 kernel: [59414.567890] [CRITICAL] Hardware event. This is not a software error.
Jun  1 04:40:15 server-prod-01 kernel: [59415.678901] [CRITICAL] MCE: [Hardware Error]: CPU 0: Machine Check: 0 Bank 6: ee00000000800400

* Number of ERROR logs found in /home/student/projects/git/devops-journey/bash/logs/system.log
13

* Number of FATAL logs found in /home/student/projects/git/devops-journey/bash/logs/system.log
2

* Number of CRITICAL logs found in /home/student/projects/git/devops-journey/bash/logs/system.log
5

'