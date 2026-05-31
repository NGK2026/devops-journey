#!/bin/bash

# takes path of dir and lists contents

cat << EOF
which directory?
EOF

read DIR

cd $DIR
echo "navigating..."
echo
pwd
ls

exit 0