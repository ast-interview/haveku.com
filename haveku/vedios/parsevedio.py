# -*- coding: utf-8 -*-


import re

def get_vid_of_url(url):
    re_of_youku = re.compile("(?<=/v_show/id_).*(?=\.html)", re.IGNORECASE)
    re_of_tudou = re.compile("(?<=/programs/view/).*(?=/)", re.IGNORECASE)
    re_of_56com = re.compile("(?<=/v_).*(?=\.html)", re.IGNORECASE)
    
    if "youku.com" in url:
        return re_of_youku.findall(url)
    elif "tudou.com" in url:
        return re_of_tudou.findall(url)
    elif "56.com" in url:
        return re_of_56com.findall(url)
    else:
        return ""




def parse_url(url):
    pass





if __name__ == "__main__":
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
    

















































