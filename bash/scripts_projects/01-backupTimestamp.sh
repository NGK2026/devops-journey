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
    cp "$FILE" "$TARGET_FOLDER"
done

echo -e "\n===** zipping backup folder to $TARGET_PARENT **==="

# -c create -z gzip -f next argument is name of file
tar -czf "$TARGET_PARENT/bak_$TIMESTAMP.tar.gz" "$TARGET_FOLDER"

echo -e "\n===** zipping complete! **===" 
