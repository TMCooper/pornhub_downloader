from pornhub_api import PornhubApi

api = PornhubApi()

videos = api.search_videos.search_videos(
    "chechick",
    ordering="mostviewed",
    period="weekly",
    tags=["black"],
)
for vid in videos:
    print(vid.title, vid.video_id)