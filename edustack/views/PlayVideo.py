#-*- coding: utf-8 -*-

'''
Created on 2016-02-25

@author: Wu Chunlong (wcl6005@126.com)
'''

from flask import Blueprint
from flask import render_template
import json

PlayVideo = Blueprint('PlayVideo', __name__)

#http://localhost:5000/PlayVideo/PlayVideo/
@PlayVideo.route('/AngularJS_Hello/')
def mAngularJS_Hello():
    str='hello world!'
    return render_template(r"PlayVideo/AngularJS_Hello.html",str=str)

@PlayVideo.route('/PlayVideo/')
def mPlayVideo():
	#Playvideos=u'欢迎吴文相光临！'
	Playvideos= u'''{videoname: '/static/PlayVideoFils/video/范冰冰认李晨为最后男友 男方承诺必大婚.mp4' ,img:'/static/PlayVideoFils/img/p1.jpg',playnum:'65',intvideo: '支持中文1'},
	 {videoname: '/static/PlayVideoFils/video/布娃娃.mp4',img:'/static/PlayVideoFils/img/p1.jpg',playnum:'89',intvideo:'支持中文2'}, 
     {videoname: '/static/PlayVideoFils/video/美女杠铃.mp4' ,img:'/static/PlayVideoFils/img/p1.jpg',playnum:'88',intvideo: '支持中文3'},
	 {videoname: '/static/PlayVideoFils/video/范冰冰认李晨为最后男友 男方承诺必大婚.mp4' , img:'/static/PlayVideoFils/img/p1.jpg', playnum:'68',intvideo: '支中持文4'},	
	 {videoname: '/static/PlayVideoFils/video/布娃娃.mp4',img:'/static/PlayVideoFils/img/p1.jpg',playnum:'89',intvideo:'支持中文2'}, 
     {videoname: '/static/PlayVideoFils/video/美女杠铃.mp4' ,img:'/static/PlayVideoFils/img/p1.jpg',playnum:'88',intvideo: '支持中文3'},
	 {videoname: '/static/PlayVideoFils/video/Flask 操作数据库.mp4' , img:'/static/PlayVideoFils/img/p1.jpg', playnum:'68',intvideo: '支中持文4'},	'''


	return render_template(r"PlayVideo/PlayVideo.html",Playvideos=Playvideos)


