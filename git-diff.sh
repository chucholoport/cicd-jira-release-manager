#!/bin/bash

# os variables
tmp=./tmp
out=$tmp/git-diff.csv

# check output folder
if [ ! -d $tmp ]; then
    mkdir $tmp
fi

# select case
# 1. tail provided
if [ $# -eq 1 ]; then
    tail=$1
    head=HEAD
    range=$tail..$head
# 2. tail & head provided
elif [ $# -eq 2 ]; then
    tail=$1
    head=$2
    range=$tail..$head
# 3. none provided
else
    tail="Initial commit"
    head="HEAD"
    range=""
fi

# execute log command
echo getting list of commits included between $tail and $head
git log $range --pretty=format:'"%h","%ad","%an","%s"' --date=iso-strict > $out
echo done.
echo 