#!/bin/bash

: <<'END_COMMENT'
Customer exported long list of LDAP usernames, stored in file called ldapusers.
Extract username only and write them to a new file.
Based on new file, create local user accounts for each user.
END_COMMENT

# Test sample
EXAMPLE="cn=lisa17,dc=example,dc=com"

echo $EXAMPLE

# Pattern match, remove longest match after comma " , "
EXAMPLE=${EXAMPLE%%,*}

echo ${EXAMPLE#cn=}

# read file line by line with while loop
while read line; do
	echo "${line%%,*}" >> 1-user_output.txt
done < 1-ldapusers.txt

# print user_output.txt
cat 1-user_output.txt
