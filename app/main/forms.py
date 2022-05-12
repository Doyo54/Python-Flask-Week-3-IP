from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,TextAreaField
from wtforms.validators import DataRequired
from ..models import Pitch


class CreatePitch(FlaskForm):
    name = StringField('Your Name',validators=[DataRequired()])
    title = StringField('Title',validators =[DataRequired()])
    category = SelectField('Category', choices=[('Food','Food'),('Movies','Movies'),('Politics','Politics'),('History','History'),('Advertisement','Advertisement')],validators=[DataRequired()])
    post = StringField('Pitch',validators =[DataRequired()])
    submit = SubmitField('Submit Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')
    
class UpvoteForm(FlaskForm):
	submit = SubmitField()


class Downvote(FlaskForm):
	submit = SubmitField()