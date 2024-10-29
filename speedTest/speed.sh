#!/bin/bash

declare -a data=`ping 8.8.8.8 -c 10 |grep avg |sed 's/\//\
	/g'`
# mapfile -t my_array < <( ping 8.8.8.8 -c 10 |grep avg |sed 's/\//\
        # /g'`)
echo $data
