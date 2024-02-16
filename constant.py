import configparser
import os


parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), "config/config.local"))

PLAYLIST_ID = parser.get("youtube", "PLAYLIST_ID")
YOUTUBE_API_KEY = parser.get("youtube", "API_KEY")
# print(YOUTUBE_API_KEY)
