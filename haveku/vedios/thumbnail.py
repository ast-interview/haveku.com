#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, hashlib, time

from urllib import request


def parse_json_from_web_interface(domain, vid):
    if domain.lower() == "youku.com":
        url = r'http://v.youku.com/player/getPlayList/VideoIDS/%s' % vid
    elif domain.lower() == "tudou.com":
        url = r'http://api.tudou.com/v6/video/info?app_key=225d19f553bde37e&format=json&itemCodes=%s' % vid
    elif domain.lower() == "56.com":
        ts = str(int(time.time()))
        
        appkey = "3000004324"
        appsecret = "3b361ba0d77e7311"
        
        m = hashlib.md5()
        s = "vid=%s" % vid
        m.update(s.encode(encoding='utf_8', errors='strict'))
        sign1 = m.hexdigest()
        
        m = hashlib.md5()
        s = "%s#%s#%s#%s" %(sign1, appkey, appsecret, ts)
        m.update(s.encode(encoding='utf_8', errors='strict'))
        sign = m.hexdigest()
        
        url = r'http://oapi.56.com/video/getVideoInfo.json?appkey=%s&sign=%s&ts=%s&vid=%s' % (appkey, sign, ts, vid)
    else:
        return "ERROR!"
    
    
    readstring = request.urlopen(url).read()
    
    return json.loads(readstring.decode('utf-8'))


def get_thumbnail_from_web_interface(domain, vid):
    
    json_dict = parse_json_from_web_interface(domain, vid)
    
    if domain.lower() == "youku.com":
        if 'data' in json_dict.keys():
            if 'logo' in json_dict['data'][0].keys():
                return json_dict['data'][0]['logo']
    
    if domain.lower() == "tudou.com":
        if 'results' in json_dict.keys():
            if 'bigPicUrl' in json_dict['results'][0].keys():
                return json_dict['results'][0]['bigPicUrl']
    
    if domain.lower() == "56.com":
        if '0' in json_dict.keys():
            if 'mimg' in json_dict['0'].keys():
                return json_dict['0']['mimg']
    
    return "ERROR!"






if __name__ == "__main__":
    
    print(get_thumbnail_from_web_interface("youku.com", 'XMzM5NTU2MDcy'))
    print(get_thumbnail_from_web_interface("tudou.com", 'f6I9_UWl5Yo'))
    print(get_thumbnail_from_web_interface("56.com", 'MTExODU1NTI5'))
    
    
    
    






























