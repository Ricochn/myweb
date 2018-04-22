from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    body = TextAreaField("文章：", validators=[DataRequired()])
    submit = SubmitField("提交")

class DeleteForm(FlaskForm):
    id = IntegerField("删除文章的id:")
    submit = SubmitField("删除")