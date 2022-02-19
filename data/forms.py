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
    icon_1 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_1 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_2 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_3 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_4 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_5 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_6 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_7 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_8 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_9 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_10 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_11 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_12 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_13 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_14 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_15 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_16 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_17 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_18 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_19 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    image_20 = FileField('Header Image', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Отправить")


class Test2(FlaskForm):
    string = StringField("Строка", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    boolean = BooleanField("TF поле")
    select = SelectField(choices=((1, "one"), (2, "two"), (3, "three")))
    submit = SubmitField("Отправить")
