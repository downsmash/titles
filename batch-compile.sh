#!/bin/bash

CHANNELS=channels
CACHE=cache
VIDEOS=videos.tsv


touch $CHANNELS $CACHE $VIDEOS

for channel in $(cat $CHANNELS); do
    echo $channel
    if ! grep -q $channel $CACHE; then
        youtube-dl --get-filename  -o "%(id)s<<>>%(title)s<<>>%(channel_id)s<<>>%(uploader)s"  "https://youtube.com/channel/$channel" | sed -u -e "s/<<>>/\t/g" | tee -a videos.tsv
        echo $channel >> $CACHE
    fi
done
