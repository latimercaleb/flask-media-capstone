from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PostsForm(FlaskForm):
    title = StringField('Email', validators=[DataRequired()])
    content = TextAreaField('Password', validators=[DataRequired()])
    submit = SubmitField('Post')