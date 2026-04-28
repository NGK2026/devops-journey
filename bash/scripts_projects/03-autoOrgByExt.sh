#!/bin/bash

# Auto-organizes files in a folder by extension into subfolders

TARGET_FOLDER="/home/student/projects/git/devops-journey/bash/scripts_projects/ext_folder"
mkdir -p "$TARGET_FOLDER"

# save file data in array
FULL_NAME_ARRAY=()
NAME_ARRAY=()
EXT_ARRAY=()
NEW_TARGET=()

for FILE in "$TARGET_FOLDER"/*; do
    FULL_NAME=$(echo "$FILE" | awk -F/ '{print $NF}')
    FILE_NAME=$(echo "$FILE" | awk -F/ '{print $NF}' | awk -F. '{print $1}')
    EXT=$(echo "$FILE" | awk -F. '{print $2}')
    
    # echo "$EXT"
    FULL_NAME_ARRAY+=("$FULL_NAME")
    NAME_ARRAY+=("$FILE_NAME")
    
    # check if ext is array, if not then add.
    if [[ ! " ${EXT_ARRAY[*]} " =~ " $EXT " ]]; then
        EXT_ARRAY+=("$EXT")
    fi

    echo "File: $FULL_NAME | File Name: $FILE_NAME | Extension: $EXT"
done

# create folders
for EXT in ${EXT_ARRAY[@]}; do
    # echo "$EXT"
    mkdir -p "$TARGET_FOLDER"/"$EXT"
    echo "** created '$TARGET_FOLDER/$EXT'"
    NEW_TARGET+='$TARGET_FOLDER/$EXT'
    # FOLDER=$(echo "$TARGET_FOLDER/$EXT" | awk -F/ '{print $(NF-1) "/" $NF}')
    # echo "$FOLDER"
done

# move files in folders respectively 
for FILE in ${FULL_NAME_ARRAY[@]}; do
    FILE_EXT=$(echo $FILE | awk -F. '{print $NF}')
    FILE_N=$(echo $FILE | awk -F. '{print $(NF-1)}')
    for TARGET in ${NEW_TARGET[@]}; do
        TARGET_EXT=$(echo $TARGET | awk -F/ '{print $NF}')
        TARGET_N=$(echo $TARGET | awk -F/ '{print $(NF-1) "/" $NF}')
        echo "()()() COMPARE: '$FILE_EXT' vs '$TARGET_EXT'"
        if [[ "$FILE_EXT" == "$TARGET_EXT" ]]; then
            mv "$FILE" "$TARGET"
            echo "{}{}{}moved '$FILE_N' to '$TARGET_N'"
        fi
    done
done

echo -e "\n\n==================================="
echo -e "=========== DONE ==========="
echo -e "==================================="

    