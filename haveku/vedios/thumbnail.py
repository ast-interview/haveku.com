#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, re, json, hashlib, time


def preview_youku(vid):
    url = r'http://v.youku.com/player/getPlayList/VideoIDS/%s' % vid
    
    '''
    proxy = urllib2.ProxyHandler({'http': r'http://SCHENKER-ASIA\hewang:Iawywfnh2@sscproxy.ap.signintra.com:80'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    '''
    
    readstring = urllib2.urlopen(url).read()
    
    dic = json.loads(readstring)
    if dic.has_key('data'):
        if dic['data'][0].has_key('logo'):
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
    
    readstring = urllib2.urlopen(url).read()
    
    dic = json.loads(readstring)
    if dic.has_key('results'):
        if dic['results'][0].has_key('bigPicUrl'):
            return dic['results'][0]['bigPicUrl']
    
    return ""


def previe_56(vid):
    '''
    http://dev.56.com/wiki/index.php?doc-view-20
    '''
    ts = unicode(int(time.time()))
    
    appkey = "3000004324"
    appsecret = "3b361ba0d77e7311"
    
    m = hashlib.md5()
    m.update("vid=%s" % vid)
    sign1 = m.hexdigest()
    
    m = hashlib.md5()
    m.update("%s#%s#%s#%s" %(sign1, appkey, appsecret, ts))
    sign = m.hexdigest()
    
    '''
    proxy = urllib2.ProxyHandler({'http': r'http://SCHENKER-ASIA\hewang:Iawywfnh2@sscproxy.ap.signintra.com:80'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    '''
    
    url = r'http://oapi.56.com/video/getVideoInfo.json?appkey=%s&sign=%s&ts=%s&vid=%s' % (appkey, sign, ts, vid)
    readstring = urllib2.urlopen(url).read()
    
    dic = json.loads(readstring)
    if dic.has_key('0'):
        if dic['0'].has_key('mimg'):
            return dic['0']['mimg']
    
    return ""






if __name__ == "__main__":
    #print preview_youku('XMzM5NTU2MDcy')
    print preview_tudou('f6I9_UWl5Yo')
    #print previe_56('MTExODU1NTI5')






























