from flask import render_template,request,redirect,url_for
from . import main
from datetime import datetime
from time import time, sleep
from .forms import BlogFormI, CommentForm, EmailFormI
from ..models import User, BLOG, Comment
from flask_login import login_required, current_user
from ..email import mail_message
import requests
import json

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to the blog app'
    return render_template("index.html", title=title)

@main.route('/theblog',methods = ['GET', 'POST'])
@login_required
def theblog():

    blog_form = BlogFormI()


    if blog_form.validate_on_submit():
        title = blog_form.title.data
        pitch = blog_form.pitch.data

        new_pitch = BLOG(m_blog_title = title, m_blog_content=pitch, m_blog_posted_on = datetime.now() , user = current_user)
        new_pitch.save_blog()

        #mail_message("Thank you for sending your first post","email/welcome_user",user.email,user=user)
        return redirect(url_for('main.theblog'))


    all_pitches = BLOG.get_all_blogs()

    return render_template("theblog.html", pitch_form = blog_form, pitches = all_pitches)

@main.route('/allblog')
def allblog():

    subscribe_frm = EmailFormI()
    random = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    all_pitches = BLOG.get_all_blogs()
    return render_template("allblog.html",pitches = all_pitches,random = random,pitch_form1 = subscribe_frm)

@main.route('/comments/<int:id>',methods = ['GET','POST'])
def pitch(id):

    my_pitch = BLOG.query.get(id)
    comment_form = CommentForm()

    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comment(c_content = comment_data, c_blog_id = id, c_com_posted_on = datetime.now())
        new_comment.save_comment()

        return redirect(url_for('main.pitch',id=id))

    all_comments = Comment.get_comments(id)

    title = 'Comment Section'
    return render_template('comment.html',pitch = my_pitch, comment_form = comment_form, comments = all_comments, title = title)
