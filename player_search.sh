#!/bin/sh

vid=$(sort -R videos.tsv | head -n1 | cut -f2)
echo $vid
while read line; do
    if grep -Fwiq "$line" <<< "$vid"; then
        echo $line
    fi
done < players_clean.txt
