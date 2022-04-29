from youtube_json import YoutubeJson


if __name__ == '__main__':
    keyword = input('keyword: ')
    yj = YoutubeJson()
    videos = yj.search_videos(keyword)
    yj.print_json(videos)
