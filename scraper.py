import requests
import instaloader
import string
class Scraper:
    def __init__(self, username, start = '', stop = ''):
        if len(start) < 1:
            start = ''
        if len(stop) < 1:
            stop = ''
        self.username = username
        L = instaloader.Instaloader()

        try:
            profile = instaloader.Profile.from_username(L.context, username)
            posts = profile.get_posts()
        except:
            posts = []
        text = ""
        max_posts = 100
        post_num = 0
        for p in posts:
            post = p.caption
            if post == None:
                continue
            if(start not in post or stop not in post):
                continue
            post_num += 1
            if(post_num > max_posts):
                break
            if(len(start) > 1):
             post = post.split(start)[1]
            if(len(stop) > 1):
             post = post.split(stop)[0]
            while(post[-1] == '\n' or post[-1] == ' '):
                post = post[:-1]
            if(post[-1] not in string.punctuation):
                post += '.'
            post += '\n'
            text +=  post
        self.text = text
