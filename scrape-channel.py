import argparse
import json
import os
from time import sleep

import googleapiclient.discovery

dev_key = "AIzaSyAY2x5lwTzwHsp3AMQjRUH3mE_q4oOL9mQ"
def __main__():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=dev_key)

    parser = argparse.ArgumentParser()
    parser.add_argument("id", type=str, help="id of channel to scrape")
    parser.add_argument("--limit", metavar="N", type=int, default=500, help="maximum number of videos to scrape")
 
    args = parser.parse_args()
 
    channel_request = youtube.channels().list(id=args.id,part="contentDetails")
    channel_response = channel_request.execute()

    channels = channel_response['items']

    # This should really be unique but let's loop anyway.
    for channel in channels:
        uploads_id = channel['contentDetails']['relatedPlaylists']['uploads']

        next_page = True
        page_token = None
        while next_page:
            uploads_request = youtube.playlistItems().list(playlistId=uploads_id,
                                                           pageToken=page_token,
                                                           part="contentDetails",
                                                           maxResults=5)
            uploads_response = uploads_request.execute()

            videos = uploads_response['items']
            for video in videos:
                video_id = video['contentDetails']['videoId']

                video_request = youtube.videos().list(id=video_id,
                                                      part="snippet")
                video_response = video_request.execute()

                print(video_id, video_response['items'][0]['snippet']['title'], sep="\t", flush=True)

            next_page = ('nextPageToken' in uploads_response.keys())
            if next_page:
                page_token = uploads_response['nextPageToken']

            sleep(1)

if __name__ == "__main__":
    __main__()
