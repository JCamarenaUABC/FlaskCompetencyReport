from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ReviewForm (FlaskForm):
    IdProduct = StringField("IdProduct:", validators=[DataRequired()])
    Comment = StringField("Comment:", validators=[DataRequired()])
    submit = SubmitField("Submit")
