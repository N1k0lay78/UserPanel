from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import PasswordField, StringField, SubmitField, BooleanField, FileField, SelectField
from wtforms.validators import DataRequired, Length


class FormRegister(FlaskForm):
    fullname = StringField("Ваше имя", validators=[DataRequired()])
    nickname = StringField("Никнейм", validators=[DataRequired()])
    email = StringField("Почта", validators=[DataRequired()])
    password_1 = PasswordField("Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()])
    password_2 = PasswordField("Повторите Пароль", validators=[Length(8, 16, "Пароль от 8 до 16 символов"), DataRequired()])
    submit = SubmitField("Зарегистрироваться")


class FormLogin(FlaskForm):
    email = StringField("Почта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


class Edit(FlaskForm):
    header_img = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])


class Test(FlaskForm):
    submit = SubmitField("Отправить")


class Test2(FlaskForm):
    string = StringField("Строка", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    boolean = BooleanField("TF поле")
    select = SelectField(choices=((1, "one"), (2, "two"), (3, "three")))
    submit = SubmitField("Отправить")
