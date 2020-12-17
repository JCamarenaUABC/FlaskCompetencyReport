from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ProductForm (FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    price = StringField("How much :", validators=[DataRequired()])
    category = StringField("Category :", validators=[DataRequired()])
    description = StringField("Description :", validators=[DataRequired()])
    submit = SubmitField("Submit")
