#!/bin/bash

# to test pattern match, use /usr/bin/hello

filename=${1#*/}
echo 'filename=${1#*/}'
echo "The name of the file is $filename"

directoryname=${1%%/*}
echo 'directoryname=${1%%/*}'
echo "the name of the directory is $directoryname"