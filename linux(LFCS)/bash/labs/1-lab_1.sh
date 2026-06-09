#!/bin/bash

: <<'END_COMMENT'
Customer exported long list of LDAP usernames, stored in file called ldapusers.
Extract username only and write them to a new file.
Based on new file, create local user accounts for each user.
END_COMMENT

EXAMPLE="cn=lisa17,dc=example,dc=com"

echo $EXAMPLE

EXAMPLE=${EXAMPLE%%,*}

echo ${EXAMPLE#cn=}

