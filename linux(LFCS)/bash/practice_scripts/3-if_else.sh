#!/bin/bash

if [ -z $1 ] 
# if test -z $1 (same as previous line but with test command)
then
	echo you have to provide an argument
	exit 6
fi

echo the argument is $1
