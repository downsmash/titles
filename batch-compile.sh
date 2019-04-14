#!/bin/bash

CHANNELS=${1:-channels}
CACHE=${2:-cache}
VIDEOS=${3:-videos.tsv}
SEP='<<>>'

touch $CHANNELS $CACHE $VIDEOS

for channel in $(cat $CHANNELS); do
    echo $channel
    if ! grep -q $channel $CACHE; then
        youtube-dl --get-filename  -o "%(id)s$SEP%(title)s$SEP%(channel_id)s$SEP%(uploader)s"  "https://youtube.com/channel/$channel" | sed -u -e "s/$SEP/\t/g" | tee -a videos.tsv
        echo $channel >> $CACHE
    fi
done
