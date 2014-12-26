# -*- coding: utf-8 -*-

import json, hashlib, time, re

from urllib import request


def get_vid_of_url(url):
    re_of_youku = re.compile("(?<=/v_show/id_).*(?=\.html)", re.IGNORECASE)
    re_of_tudou = re.compile("(?<=/programs/view/).*(?=/)", re.IGNORECASE)
    re_of_56com = re.compile("(?<=/v_).*(?=\.html)", re.IGNORECASE)
    
    if "youku.com" in url:
        return re_of_youku.findall(url)[0]
    elif "tudou.com" in url:
        return re_of_tudou.findall(url)[0]
    elif "56.com" in url:
        return re_of_56com.findall(url)[0]
    else:
        return ""


def parse_json_from_web_interface(url, vid):
    if "youku.com" in url.lower():
        parse_url = r'http://v.youku.com/player/getPlayList/VideoIDS/%s' % vid
    elif "tudou.com" in url.lower():
        parse_url = r'http://api.tudou.com/v6/video/info?app_key=225d19f553bde37e&format=json&itemCodes=%s' % vid
    elif "56.com" in url.lower():
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
        
        parse_url = r'http://oapi.56.com/video/getVideoInfo.json?appkey=%s&sign=%s&ts=%s&vid=%s' % (appkey, sign, ts, vid)
    else:
        return "ERROR!"
    
    
    readstring = request.urlopen(parse_url).read()
    
    return json.loads(readstring.decode('utf-8'))


def get_data_from_web_interface(url):
    
    json_dict = parse_json_from_web_interface(url, get_vid_of_url(url))
    
    try:
        if "youku.com" in url.lower():
            return [
                    json_dict['data'][0]['title'],
                    "",
                    json_dict['data'][0]['logo']
                    ]
        
        if "tudou.com" in url.lower():
            return [
                    json_dict['results'][0]['title'],
                    json_dict['results'][0]['description'],
                    json_dict['results'][0]['bigPicUrl']
                    ]
        
        if "56.com" in url.lower():
            return [
                    json_dict['0']['title'],
                    json_dict['0']['desc'],
                    json_dict['0']['mimg']
                    ]
    
    except:
        return ""
    
    return ""



if __name__ == "__main__":
    pass
    
    #url = "http://v.youku.com/v_show/id_XODU0MzA4NzI0.html?ev=5&from=y1.1-2.10001-0.1-2"
    
    #print(get_data_from_web_interface(url))
    '''
    url = "http://v.youku.com/v_show/id_XODU0MzA4NzI0.html?ev=5&from=y1.1-2.10001-0.1-2"
    re_of_youku = re.compile("(?<=/v_show/id_).*(?=\.html)", re.IGNORECASE)
    vid = re_of_youku.findall(url)
    print(vid)
    
    url = "http://www.tudou.com/programs/view/YzIFnviBarw/?fr=rec2"
    re_of_tudou = re.compile("(?<=/programs/view/).*(?=/)", re.IGNORECASE)
    vid = re_of_tudou.findall(url)
    print(vid)
    
    url = "http://www.56.com/u63/v_MTI4OTgxNjUy.html"
    re_of_56com = re.compile("(?<=/v_).*(?=\.html)", re.IGNORECASE)
    vid = re_of_56com.findall(url)
    print(vid)
    
    print(get_vid_of_url(url))
    '''

















































