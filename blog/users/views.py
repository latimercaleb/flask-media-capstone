from flask import render_template, request, Blueprint, url_for, redirect, flash, request
from flask_wtf import FlaskForm
from flask_login import login_user, logout_user, login_required, current_user
from blog import db, login_manager
from blog.models import User
from blog.users.forms import LoginForm, RegistrationForm, UpdateForm
from blog.users import save_picture
users = Blueprint('users', __name__, template_folder='templates')

# TODO: Integrate routes for user controller flow
