#!python3
#encoding:utf-8
import json
import time
from urllib.parse import urlparse
#import furl
class Response:
    def __init__(self):
        pass
    def Get(self, r, type=None, success_code=None, sleep_time=2, is_show=True):
        if is_show:
            print("HTTP Status Code: {0}".format(r.status_code))
            print(r.text)
        time.sleep(sleep_time)
        if None is not success_code:
            if (success_code != r.status_code):
                raise Exception('HTTP Error: {0}'.format(r.status_code))
                return None
        if 'json' == type.lower():
            return json.loads(r.text)
        elif 'binary' == type.lower():
            return r.content
        else:
            return r.text
    def GetLink(self, r, rel='next'):
        if None is r.links:
            return None
        if 'next' == rel or 'prev' == rel or 'first' == rel or 'last' == rel:
            return r.links[rel]['url']
    def GetLinkNext(self, r):
        return self.__get_page(r, 'next')
    def GetLinkPrev(self, r):
        return self.__get_page(r, 'prev')
    def GetLinkFirst(self, r):
        return self.__get_page(r, 'first')
    def GetLinkLast(self, r):
        return self.__get_page(r, 'last')
    def __get_page(self, r, rel='next'):
        if None is r:
            return None
        print(r.links)
        if rel in r.links.keys():
            url = urlparse(r.links[rel]['url'])
            print(url.query['page'])
            return url.query['page']
            """
            f = furl(r.links[rel]['url'])
            print(f.query['page'])
            return f.query['page']
            """
        else:
            return None
