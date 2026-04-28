#!/bin/bash

# Auto-organizes files in a folder by extension into subfolders

TARGET_FOLDER="/home/student/projects/git/devops-journey/bash/scripts_projects/ext_folder"
mkdir -p "$TARGET_FOLDER"

# save extensions in array
EXT_ARRAY=()
for FILE in "$TARGET_FOLDER"/*; do
    EXT=$(echo "$FILE" | awk -F. '{print $2}')
    # echo "$EXT"
    EXT_ARRAY+=("$EXT")
    echo "File: $FILE | Extension: $EXT"
done