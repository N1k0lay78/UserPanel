from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import PasswordField, StringField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, Length


class FormLogin(FlaskForm):
    # login = StringField("Почта/Логин")
    password = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов")])
    # autologin = BooleanField("Сохранить аккаунт")
    submit = SubmitField("Войти")


class Edit():
    header_img = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
