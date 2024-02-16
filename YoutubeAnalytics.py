import json
import requests
from constant import YOUTUBE_API_KEY
from pprint import pprint
from kafka import KafkaProducer

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
    response = requests.get(
        "https://www.googleapis.com/youtube/v3/videos",
        params={
            "key": YOUTUBE_API_KEY,
            "id": "HwgrFT2o4LQ",
            "part": "snippet, statistics, status",
        },
    )
    # print(response.text)
    response = json.loads(response.text)["items"]
    for video in response:
        video_res = {
            "title": video["snippet"]["title"],
            "likes": int(video["statistics"].get("likeCount", 0)),
            "comments": int(video["statistics"].get("commentCount", 0)),
            "views": int(video["statistics"].get("viewsCount", 0)),
            "favorites": int(video["statistics"].get("favoriteCount", 0)),
            "thumbnail": video["snippet"]["thumbnails"]["default"]["url"],
        }

        pprint(video_res)
        producer.send("youube_videos", json.dumps(video_res).encode("utf-8"))

        producer.flush()
