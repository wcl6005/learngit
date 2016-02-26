# -*- coding: utf-8 -*-

'''
Created on 2016-01-17

@author: Wu Wenxiang (wuwenxiang.sh@gmail.com)

中国
'''

from flask import Blueprint ,request
from flask import render_template
from edustack.models import User
from edustack.models import Blog
from edustack.models import Comment
from edustack.views.api import _get_blogs_by_page
test = Blueprint('test', __name__)

def _get_page_index():
    pageIndex = request.args.get('page', '1')
    try:
        pageIndex = int(pageIndex)
    except:
        pageIndex = 1
    return pageIndex


#http://localhost:5000/test/test1234/
@test.route('/')
@test.route('/test/')
def hello():
    pageIndex = _get_page_index()
    blogs, page = _get_blogs_by_page(pageIndex)
    return render_template(r"home/blogs.html", blogs=blogs, page=page)


@test.route('/')
@test.route('/smoketest/')
def msmoketest():
    users = User.query.all()
    blogs = Blog.query.all()
    comments = Comment.query.all()
    return render_template(r"test/smoketest.html",users=users,
                           blogs=blogs, comments=comments)


#Angularjs  http://localhost:5000/test/testangularjs/
@test.route('/')
@test.route('/testangularjs/')
def testangularjs():
    str=u'欢迎吴春龙光临！'
    return render_template(r"test/testangularjs.html",str=str)

#测试注册用户信息
@test.route('/')
@test.route('/testuser/')
def testuser():
    users = User.query.all()
    return render_template(r"test/testuser.html",users=users)    