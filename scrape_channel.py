import argparse
import os
from time import sleep

import googleapiclient.discovery

DEV_KEY = "YOUR_KEY_HERE"

def scrape_channel(channel_id):
    """Print a list of uploads from _channel_id_ to stdout.
    """
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=DEV_KEY)

    channel_request = youtube.channels().list(id=channel_id, part="contentDetails")
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

                print(video_id, video_response['items'][0]['snippet']['title'],
                      sep="\t", flush=True)

            next_page = ('nextPageToken' in uploads_response.keys())
            if next_page:
                page_token = uploads_response['nextPageToken']

            sleep(1)


def __main__():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    parser = argparse.ArgumentParser()
    parser.add_argument("id", type=str, help="id of channel to scrape")

    args = parser.parse_args()
    scrape_channel(args.id)


if __name__ == "__main__":
    __main__()
