#!/bin/bash

CHANNELS=${1:-channels}
CACHE=${2:-cache}
VIDEOS=${3:-videos.tsv}
SEP='<<>>'

red="$(tput setaf 1)"
reset="$(tput sgr0)"

touch $CHANNELS $CACHE $VIDEOS

for channel in $(cat $CHANNELS); do

  if grep -q $channel $CACHE; then
    count="$(printf '%5d' $(grep -c $channel $VIDEOS))"
    echo -e "$red($(date '+%x %X'))$reset\tParsed $count videos from $channel"
  else
    echo -e "$red[$(date '+%x %X')]$reset\tNow parsing $channel"
    youtube-dl --get-filename  -o "%(id)s$SEP%(title)s$SEP%(channel_id)s$SEP%(uploader)s"  "https://youtube.com/channel/$channel" | sed -u -e "s/$SEP/\t/g" | tee -a videos.tsv
    echo $channel >> $CACHE
  fi
done
