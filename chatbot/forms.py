from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField

# Makale formu
class ArticleForm(FlaskForm):
    title = StringField('Title')
    content = TextAreaField('Content')
    image = FileField('Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])