from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ReviewForm (FlaskForm):
    idproduct = StringField("Id Product:", validators=[DataRequired()])
    comment = StringField("Comment:", validators=[DataRequired()])
    submit = SubmitField("Submit")
