from pytube import Search
import json


class YoutubeJson:

    def search_videos(self, keyword: str) -> list:
        videos = []
        s = Search(keyword)
        results = s.results
        for result in results:
            video = {
                'title': result.title,
                'url': 'https://www.youtube.com/watch?v=' + result.video_id,
                'video_id': result.video_id,
                'thumbnail_url': result.thumbnail_url
            }
            videos.append(video)
        return videos

    def print_json(self, videos: list) -> None:
        json_str = json.dumps(videos)
        data = json.loads(json_str)
        print(json.dumps(data, indent=4, ensure_ascii=False))
