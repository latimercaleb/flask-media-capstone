from flask import render_template, request, Blueprint 
from blog.posts.forms import PostsForm
from flask import render_template, request, Blueprint, url_for, redirect, flash, request, abort
from flask_wtf import FlaskForm
from flask_login import login_user, logout_user, login_required, current_user
from blog import db, login_manager
from blog.models import User, Post

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/add', methods=['GET', 'POST'])
@login_required
def add_post():
    form = PostsForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        flash('New Post!')
        return redirect(url_for('core.index'))
    return render_template('add_post.html', post_form=form)

@posts.route('/<int:post_id>') # Cast param to int
def render_posts(post_id):
    user_post = Post.query.get_or_404(post_id)
    return render_template('single_post.html', post_details= user_post)

# Update in prog
@posts.route('/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    user_post = Post.query.get_or_404(post_id)
    if user_post != current_user:
        abort(403)
    form = PostsForm()
    if form.validate_on_submit():
        user_post.title = form.title.data
        user_post.content = form.content.data
        db.session.commit()
        flash('Post Editted!')
        return redirect(url_for('posts.render_posts', post_id = user_post.id))
    elif request.method == 'GET':
       form.title.data = user_post.title
       form.content.data = user_post.content
    return render_template('add_post.html', post_form=form)

# Delete in prog
@posts.route('/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    user_post = Post.query.get_or_404(post_id)
    if user_post != current_user:
        abort(403)
    db.session.delete(user_post)
    db.session.commit()
    flash('Post deleted')
    return redirect(url_for('core.index'))

