'''
Created on 2016-02-25

@author: Wu Chunlong (wcl6005@126.com)
'''

from flask import Blueprint
from flask import render_template


PlayVideo = Blueprint('PlayVideo', __name__)



#http://localhost:5000/PlayVideo/PlayVideo/
@PlayVideo.route('/AngularJS_Hello/')
def mAngularJS_Hello():
    str='hello world!'
    return render_template(r"PlayVideo/AngularJS_Hello.html",str=str)

@PlayVideo.route('/PlayVideo/')
def mPlayVideo():
    str='PlayVideo!'
    return render_template(r"PlayVideo/PlayVideo.html",str=str)

#@PlayVideo.route('/PlayVideo/')
#def mPlayVideo():
#    str='hello world!'
#    return render_template(r"PlayVideo/PlayVideo.html",str=str)
