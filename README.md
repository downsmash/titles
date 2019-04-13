# titles
YouTube scraper and video title classifier for the [Downsmash](downsma.sh) project.

## Prerequisites
###  Scraper
- A recent ([>2014.07.25](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#faq)) version of youtube-dl.
- If you want to run the Python scraper (scrape_channel.py), you'll need the Google API client libraries. Note that the daily call limit has been [drastically lowered](https://stackoverflow.com/questions/15568405/youtube-api-limitations), so you won't be able to run it for more than about 15 minutes per day unless you have an API account that predates this limit (January 2019 or earlier.)

## Usage

### Scraper
```
$ ./batch-compile.sh channels cache videos.tsv
```

### Trainer
TODO

### Classifier
TODO
