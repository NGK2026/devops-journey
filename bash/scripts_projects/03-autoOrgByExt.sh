#!/bin/bash

# Auto-organizes files in a folder by extension into subfolders

TARGET_FOLDER="/home/student/projects/git/devops-journey/bash/scripts_projects/ext_folder"
mkdir -p "$TARGET_FOLDER"

# create files
touch "$TARGET_FOLDER"/{1.sh,2.sh,3.sh,4.txt,5.txt,6.html,7.py,8.py,9.html,10.txt,11.docx,12.csv,13.csv,14.docx,15.pdf}
echo "Created files"

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
    FULL_NAME_ARRAY+=("$FILE")
    NAME_ARRAY+=("$FILE_NAME")
    
    # check if ext is array, if not then add.
    if [[ ! " ${EXT_ARRAY[*]} " =~ " $EXT " ]]; then
        EXT_ARRAY+=("$EXT")
    fi

    echo "File: $FILE | File Name: $FILE_NAME | Extension: $EXT"
done

# create folders
for EXT in ${EXT_ARRAY[@]}; do
    # echo "$EXT"
    mkdir -p "$TARGET_FOLDER"/"$EXT"
    echo "** created '$TARGET_FOLDER/$EXT'"
    NEW_TARGET+=("$TARGET_FOLDER/$EXT")
    # FOLDER=$(echo "$TARGET_FOLDER/$EXT" | awk -F/ '{print $(NF-1) "/" $NF}')
    # echo "$FOLDER"
done

# move files in folders respectively 
for FILE_AR in ${FULL_NAME_ARRAY[@]}; do
    echo "$FILE_AR"
    FILE_EXT=$(echo $FILE_AR | awk -F. '{print $NF}')
    FILE_N=$(echo $FILE_AR | awk -F. '{print $(NF-1)}')
    for TARGET in ${NEW_TARGET[@]}; do
        # echo "$TARGET"
        TARGET_EXT=$(echo $TARGET | awk -F/ '{print $NF}')
        TARGET_N=$(echo $TARGET | awk -F/ '{print $(NF-1) "/" $NF}')
        # echo "()()() COMPARE: '$FILE_EXT' vs '$TARGET_EXT'"
        # echo "$FILE_AR"
        # echo "$TARGET"
        if [[ "$FILE_EXT" == "$TARGET_EXT" ]]; then
            mv $FILE_AR $TARGET
            echo "{}{}{}moved '$FILE_N' to '$TARGET_N'"
        fi
    done
done

echo -e "\n\n==================================="
echo -e "=========== DONE ==========="
echo -e "==================================="

    