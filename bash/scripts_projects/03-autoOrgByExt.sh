#!/bin/bash

# Auto-organizes files in a folder by extension into subfolders

TARGET_FOLDER="/home/student/projects/git/devops-journey/bash/scripts_projects/ext_folder"
mkdir -p "$TARGET_FOLDER"

# save extensions in array
EXT_ARRAY=()
for FILE in $TARGET_FOLDER/*; do
    echo "$(FILE | tr -d '.' | awk '{print $2}')"