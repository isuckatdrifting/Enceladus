import re
import requests
import json
import argparse

class LyricParser:
    def __init__(self, url):
        self.url = url
        self.prefix = 'http://music.163.com/api/song/lyric?os=pc&id='
        self.suffix = '&lv=-1&kv=-1&tv=-1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'}
        self.lyric = ''
        self.tlyric = ''

    def get_song_id(self):
        if self.url != "":
            id = re.split('id=', self.url)[1]
            return id
        else:
            return ""

    def get_lyrics(self):
        id = self.get_song_id()
        if id != "":
            link = self.prefix + id + self.suffix
            web_data = requests.get(url=link, headers=self.headers).text
            json_data = json.loads(web_data)
            self.lyric = json_data['lrc']['lyric']
            self.tlyric = json_data['tlyric']['lyric']
            try:
                return self.lyric, self.tlyric
            except BaseException:
                return "id format error, please try again"

        else:
            return "link error, please try again"

    def merge_lyrics(self):
        # Step 1: convert lyric to dict
        # print(self.lyric)
        lyric_dict = {}
        for element in self.lyric.split('\n'):
            lyric_split = list(filter(None, element.split(']')))
            if len(lyric_split) > 1:
                lyric_dict[lyric_split[0]+']'] = lyric_split[1]
        # print(lyric_dict)
        
        # Step 2: convert tlyric to dict
        # print(self.tlyric)
        tlyric_dict = {}
        for element in self.tlyric.split('\n'):
            tlyric_split = list(filter(None, element.split(']')))
            if len(tlyric_split) > 1:
                tlyric_dict[tlyric_split[0]+']'] = tlyric_split[1]
        # print(tlyric_dict)

        # Step 3: merge the two dicts
        merge_dict = {}
        for key in (lyric_dict.keys() | tlyric_dict.keys()):
            if key in lyric_dict: merge_dict.setdefault(key, []).append(lyric_dict[key])
            if key in tlyric_dict: merge_dict.setdefault(key, []).append(tlyric_dict[key])
        # print(merge_dict)

        # Step 4: print the merged dict in lyric format
        for k in sorted(merge_dict):
            print(k + "/".join(merge_dict[k]))

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("format")
    # args = parser.parse_args()
    # print(args.format)
    url = 'https://music.163.com/#/song?id=533943763'
    net = LyricParser(url)
    lyric, tlyric = net.get_lyrics()
    net.merge_lyrics()