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

# clean file
> 1-user_output.txt

# read file line by line with while loop
while read line; do
	USER=${line%%,*}
	echo ${USER#cn=} >> 1-user_output.txt
done < 1-ldapusers.txt

# print user_output.txt
cat 1-user_output.txt

# create users found in user_output file
while read line; do
	echo ___---__ creating user __---___
	echo \* \* sudo useradd -m $line \* \*
	echo ---___------ DONE ------___---
	echo
done < 1-user_output.txt





