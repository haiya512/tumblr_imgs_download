#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys
from tumblr import Tumblr

def tumblr_run(blog):
    dl = Tumblr(blog)
    dl.run()

if __name__ == "__main__":

    if len(sys.argv) == 1:
        blogs = ("sukoyaka"
                 ,"backseam"
                 ,"backseamextreme"
                 ,"beautifully"
                 ,"curvature"
                 ,"deltaso"
                 ,"emogirls"
                 ,"nico2"
                 ,"thegirlnextdoor"
                 ,"kenjikee"
                 ,"inspireawesome"
                 ,"max07min"
                 ,"keepithotfordaddy"
                 ,"labialounge"
                 ,"djangomango"
                 ,"melc"
                 ,"renka"
                 ,"milestone"
                 ,"nylonfoxie"
                 ,"onehandedtypist"
                 ,"paste"
                 ,"monorainbows"
                 ,"uhya_hya"
                 ,"unpoco"
                 ,"uratching"
                 ,"moonlightbutterflies")
    else:
        blogs = sys.argv[1:]

    for blog in blogs:
        tumblr_run(blog)
