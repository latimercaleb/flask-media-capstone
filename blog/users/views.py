from flask import render_template, request, Blueprint, url_for, redirect, flash, request
from flask_wtf import FlaskForm
from flask_login import login_user, logout_user, login_required, current_user
from blog import db, login_manager
from blog.models import User, Post
from blog.users.forms import LoginForm, RegistrationForm, UpdateForm
from blog.users.photo_handler import save_photo

users = Blueprint('users', __name__)

@users.route('/login', methods=['GET', 'POST'])
def login():
    print("Reached 3")
    form = LoginForm()
    if form.validate_on_submit():
        print("Reached 4")
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!')
            next_page = request.args.get('next') # Grab the next page attempted
            return redirect(next_page) if next_page else redirect(url_for('core.index'))
        else: 
            flash('Login failed!')
            print ("Reached 5") # Add redirect logic for login failure
    return render_template('login.html', login_form=form)

@users.route('/register', methods=['GET', 'POST'])
def register():
    # 2 problems, 1 form object is coming over incorrectly (probably because of action? Nope it was validator)
    # 2. Logging in triggers error Exception: Install 'email_validator' for email validation support.
    print("Reached")
    form = RegistrationForm()
    print(form.validate_on_submit())
    print(form.data) # {'email': None, 'username': None, 'password': None, 'confirm_password': None, 'submit': False, 'csrf_token': None}
    if form.validate_on_submit():
        print("Reached 2")
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('users.login'))
    return render_template('register.html', registration_form=form)

@login_required
@users.route('/account', methods=['GET', 'POST'])
def account():
    form = UpdateForm()
    if form.validate_on_submit():
        if form.photo.data:
            username = current_user.username
            current_user.profile_pic  = save_photo(form.photo.data,username)
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Update successful.')
        return redirect(url_for('users.account'))

    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_pic)
    return render_template('account.html', photo = profile_image, update_form=form)

@login_required
@users.route('/<username>', methods=['GET', 'POST'])
def user_posts(username):
    user_page = request.args.get('page',1,type=int) # Cycle through posts, pagination
    user = User.query.filter_by(username=username).first_or_404()
    user_posts = Post.query.filter_by(writer=user).order_by(Post.date.desc()).paginate(page=user_page, per_page=5) # TODO REview model and orm for pagination
    return render_template('user_posts.html', posts = user_posts, author=user)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))