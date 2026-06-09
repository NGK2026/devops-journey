#!/bin/bash

: <<'END_COMMENT'
Customer exported long list of LDAP usernames, stored in file called ldapusers.
Extract username only and write them to a new file.
Based on new file, create local user accounts for each user.
END_COMMENT

for i in $(cat 1-ldapusers.txt)
do
	USER=${i#*=}
	USER=${USER%%,*}
	echo useradd $USER
done
