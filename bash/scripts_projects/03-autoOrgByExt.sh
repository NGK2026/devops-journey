#!/bin/bash

# Auto-organizes files in a folder by extension into subfolders

TARGET_FOLDER="/home/student/projects/git/devops-journey/bash/scripts_projects/ext_folder"
mkdir -p "$TARGET_FOLDER"

# save extensions in array
EXT_ARRAY=()
for FILE in "$TARGET_FOLDER"/*; do
    FULL_NAME=$(echo "$FILE" | awk -F/ '{print $NF}')
    FILE_NAME=$(echo "$FILE" | awk -F/ '{print $NF}' | awk -F. '{print $1}')
    EXT=$(echo "$FILE" | awk -F. '{print $2}')
    # echo "$EXT"
    EXT_ARRAY+=("$EXT")
    echo "File: $FULL_NAME | File Name: $FILE_NAME | Extension: $EXT"
done

for EXT in ${EXT_ARRAY[@]}; do
    echo "$EXT"
    # mkdir -p "$TARGET_FOLDER"/"$EXT"
    echo "created "$TARGET_FOLDER"/"$EXT"
done