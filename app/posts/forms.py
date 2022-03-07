from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length




class PostForm(FlaskForm):
    subject = StringField('subject', validators=[DataRequired(), Length(max=50)])
    content = StringField('content', validators=[DataRequired(), Length(max=500)])
