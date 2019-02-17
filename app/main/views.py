from flask import render_template,request,redirect,url_for
from . import main
from .forms import ReviewForm, BlogFormI, CommentForm
from ..models import User, BLOG, Comment
from flask_login import login_required, current_user

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

        new_pitch = BLOG(m_blog_title = title, m_blog_content=pitch, user = current_user)
        new_pitch.save_blog()

        #return redirect(url_for('index.html'))

    title = 'Interview Pitch'
    all_pitches = BLOG.get_all_blogs()

    return render_template("theblog.html", pitch_form = blog_form, pitches = all_pitches)

@main.route('/pitch/<int:id>',methods = ['GET','POST'])
@login_required
def pitch(id):

    my_pitch = Pitch.query.get(id)
    comment_form = CommentForm()

    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comment(comment_content = comment_data, pitch_id = id, user = current_user)
        new_comment.save_comment()

        return redirect(url_for('main.pitch',id=id))

    all_comments = Comment.get_comments(id)

    title = 'Comment Section'
    return render_template('pitch.html',pitch = my_pitch, comment_form = comment_form, comments = all_comments, title = title)
