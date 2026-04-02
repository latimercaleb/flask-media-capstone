from blog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    profile_pic = db.Column(db.String(64), default="default_pic.png", nullable=False)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(80), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='writer', lazy=True)

    def __init__(self, email, username, password):
        super().__init__()
        self.email = email
        self.username = username
        self.set_password(password)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    writer=db.relationship('User', backref='posts', lazy=True)

    def __init__(self, title, content, user_id):
        super().__init__()
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'<Post {self.title} by User {self.user_id}>'