from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import PasswordField, StringField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, Length


class FormRegister(FlaskForm):
    nickname = StringField("Никнейм")
    mail = StringField("Почта")
    password_1 = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов")])
    password_2 = PasswordField("Повторите Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов")])
    submit = SubmitField("Войти")


class Edit(FlaskForm):
    header_img = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
