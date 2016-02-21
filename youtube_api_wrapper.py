from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from datetime import date
import datetime
import time


class YoutubeApiWrapper:
    def __init__(self):
        self.DEVELOPER_KEY = "AIzaSyCBA5K2YdiO1SNH0t-zQcdKGQ7Int2rwMo"
        self.YOUTUBE_API_SERVICE_NAME = "youtube"
        self.YOUTUBE_API_VERSION = "v3"
        self.youtube_build = build(self.YOUTUBE_API_SERVICE_NAME,
                                   self.YOUTUBE_API_VERSION,
                                   developerKey=self.DEVELOPER_KEY)

    def get_videos_from_channel_after_date(self, channel_id, date_after):
        argparser.add_argument("--q", help="Search term", default="Google")
        argparser.add_argument("--max-results", help="Max results", default=25)
        args = argparser.parse_args()
        options = args
        search_response = self.youtube_build.search().list(
        # channelId=channel_id,
        # part="id,snippet",
        # maxResults=options.max_results,
        # publishedAfter=date_after,
        # type="video"
            channelId=channel_id,
            part="id,snippet",
            maxResults=options.max_results,
            publishedAfter=date_after
        ).execute()
        print(search_response)


def main():
    youtube_api_wrapper = YoutubeApiWrapper()
    yesterday = datetime.date.fromordinal(datetime.date.today().toordinal()-2)

    yesterday_datetime = datetime.datetime.combine(yesterday, datetime.datetime.min.time())
    iso_time = yesterday_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        youtube_api_wrapper.get_videos_from_channel_after_date(channel_id="UCIKF1msqN7lW9gplsifOPkQ",
                                                               date_after=iso_time)
    except HttpError as e:
        print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))

main()