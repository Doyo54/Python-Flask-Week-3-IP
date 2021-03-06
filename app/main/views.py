from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment,Upvote,Downvote
from .forms import CreatePitch,CommentForm,UpdateProfile
from .. import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/pitch')
@login_required
def pitch():
    pitches = Pitch.query.all()
    return render_template('new_pitch.html', pitches = pitches)

@main.route('/food')
def food():
    food = Pitch.query.filter_by(category = 'Food').all() 
    return render_template('category/food.html', food = food)

@main.route('/movies')
def movies():
    movies = Pitch.query.filter_by(category = 'Movies').all()
    return render_template('category/movie.html', movies = movies)

@main.route('/politics')
def politics():
    politics = Pitch.query.filter_by(category = 'Politics').all()
    return render_template('category/politics.html', politics = politics)

@main.route('/history')
def history():
    history = Pitch.query.filter_by(category = 'History').all()
    return render_template('category/history.html', history = history)

@main.route('/advertisement')
def ads():
    advertisement = Pitch.query.filter_by(category = 'Advertisement').all()
    return render_template('category/ads.html', ads = advertisement)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form =CreatePitch()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        name = form.name.data
        new_pitch_object = Pitch(username=name, user_id=current_user._get_current_object().id, post=post,category=category,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.pitch'))
        
    return render_template('pitch.html', form = form)


@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)

# @main.route('/like/<int:id>',methods = ['POST','GET'])
# def like(id):
#     get_pitches = Upvote.get_upvotes(id)
#     valid_string = f'{current_user.id}:{id}'
#     for pitch in get_pitches:
#         to_str = f'{pitch}'
#         print(valid_string+" "+to_str)
#         if valid_string == to_str:
#             return redirect(url_for('pitch',id=id))
#         else:
#             continue
#     new_vote = Upvote(user = current_user, pitch_id=id)
#     new_vote.save()
#     return redirect(url_for('pitch',id=id))
@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
def like(pitch_id):
    user = current_user
    
    if Upvote.query.filter(Upvote.user_id==user.id,Upvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.pitch'))

    new_upvote = Upvote(pitch_id=pitch_id, user = current_user)
    new_upvote.save()
    return redirect(url_for('main.pitch'))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
def dislike(id):
    pitch = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in pitch:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitch',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, pitch_id=id)
    new_downvote.save()
    return redirect(url_for('main.pitch',id = id))

@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

