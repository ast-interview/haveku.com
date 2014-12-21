#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, hashlib, time

from urllib import request


def preview_youku(vid):
    url = r'http://v.youku.com/player/getPlayList/VideoIDS/%s' % vid
    
    '''
    proxy = urllib2.ProxyHandler({'http': r'http://SCHENKER-ASIA\name:pwd@sscproxy.ap.signintra.com:80'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    '''
    
    readstring = request.urlopen(url).read()
    
    
    dic = json.loads(readstring.decode('utf-8'))
    
    if 'data' in dic.keys():
        if 'logo' in dic['data'][0].keys():
            return dic['data'][0]['logo']
    
    return ""
    
    
    '''
    match = re.search('"logo":"[^"]*"', readstring)
    
    if match:
        image_url = unicode(m.group().split(":", 1)[1][1:-1]).replace(r"\/", r"/")
        return image_url
    else:
        return 'No match'
    '''
    

def preview_tudou(vid):
    url = r'http://api.tudou.com/v6/video/info?app_key=225d19f553bde37e&format=json&itemCodes=%s' % vid
    
    readstring = request.urlopen(url).read()
    
    rst = json.loads(readstring.decode('utf-8'))
    
    if 'results' in rst.keys():
        if 'bigPicUrl' in rst['results'][0].keys():
            return rst['results'][0]['bigPicUrl']
    
    return ""


def previe_56(vid):
    '''
    http://dev.56.com/wiki/index.php?doc-view-20
    '''
    ts = str(int(time.time()))
    
    appkey = "3000004324"
    appsecret = "3b361ba0d77e7311"
    
    m = hashlib.md5()
    #m.update("vid=%s" % vid)
    a = "vid=%s" % vid
    m.update(a.encode(encoding='utf_8', errors='strict'))
    sign1 = m.hexdigest()
    
    m = hashlib.md5()
    a = "%s#%s#%s#%s" %(sign1, appkey, appsecret, ts)
    m.update(a.encode(encoding='utf_8', errors='strict'))
    sign = m.hexdigest()
    
    '''
    proxy = urllib2.ProxyHandler({'http': r'http://SCHENKER-ASIA\name:pwd@sscproxy.ap.signintra.com:80'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    '''
    
    url = r'http://oapi.56.com/video/getVideoInfo.json?appkey=%s&sign=%s&ts=%s&vid=%s' % (appkey, sign, ts, vid)
    readstring = request.urlopen(url).read()
    
    dic = json.loads(readstring.decode('utf-8'))
    
    if '0' in dic.keys():
        if 'mimg' in dic['0'].keys():
            return dic['0']['mimg']
    
    return ""






if __name__ == "__main__":
#     print(preview_youku('XMzM5NTU2MDcy'))
#     print(preview_tudou('f6I9_UWl5Yo'))
    print(previe_56('MTExODU1NTI5'))






























