#!/bin/bash

# Backs up a directory to another location with a timestamp

TIMESTAMP=$(date +%F)
SOURCE_FOLDER="/home/student/projects/git/devops-journey/bash/scripts_practice"
TARGET_FOLDER="/home/student/projects/git/devops-journey/bash/scripts_projects/bak_$TIMESTAMP"
TARGET_PARENT="/home/student/projects/git/devops-journey/bash/scripts_projects"

FILES2BAK=("$SOURCE_FOLDER"/*)

# create bak dir if not exist
mkdir -p "$TARGET_FOLDER"

for FILE in "${FILES2BAK[@]}"; do
    echo -e "\n===** backing up $FILE **==="
    # -n no-clobber (dont overwrite, just skip)
    cp -n "$FILE" "$TARGET_FOLDER"
done

echo -e "\n===** zipping backup folder to $TARGET_PARENT **==="

# -c create -z gzip -f next argument is name of file -C change DIR
tar -czf "$TARGET_PARENT/bak_$TIMESTAMP.tar.gz" -C "$TARGET_PARENT" "bak_$TIMESTAMP"

echo -e "\n===** zipping complete! **===" 

: '
Output:

===** backing up /home/student/projects/git/devops-journey/bash/scripts_practice/01-analyse-logs.sh **===

===** backing up /home/student/projects/git/devops-journey/bash/scripts_practice/02-echo-lyseLogs.sh **===

===** backing up /home/student/projects/git/devops-journey/bash/scripts_practice/03-absolute-lyseLogs.sh **===

===** backing up /home/student/projects/git/devops-journey/bash/scripts_practice/04-variables-lyseLog.sh **===

===** backing up /home/student/projects/git/devops-journey/bash/scripts_practice/05-arrayVariable-lyseLog.sh **===

===** backing up /home/student/projects/git/devops-journey/bash/scripts_practice/06-loop-lyseLogs.sh **===

===** backing up /home/student/projects/git/devops-journey/bash/scripts_practice/07-conditional-lyseLogs.sh **===

===** zipping backup folder to /home/student/projects/git/devops-journey/bash/scripts_projects **===

===** zipping complete! **===
'