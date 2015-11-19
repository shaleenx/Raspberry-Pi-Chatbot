#!/bin/bash

NEWFILE=$1

for file in `ls img |sort -g -r`
do
    filename=$(basename "$file")
    extension=${filename##*.}
    filename=${filename%.*}

    if [ $filename -ge $NEWFILE ]
    then
        mv "$file" "$(($filename + 1))".$extension
    fi
done
