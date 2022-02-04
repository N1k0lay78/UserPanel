from flask import Blueprint, render_template, request
from data.forms import FormRegister
from user.logic import check_password

user = Blueprint('user', __name__, template_folder="pages")


@user.route("/")
def main():
    return render_template("test.html")


@user.route("/register/", methods=['GET', 'POST'])
def register():
    # TODO: make DB
    form = FormRegister()
    error = ""
    if request.method == 'POST':
        error, res = check_password(form.password_1.data, form.password_2.data)
        if res:
            error = "*Вход в аккаунт*"
    return render_template("login.html", form=form, error=error, form_title="Регистрация")


@user.route("/login/", methods=['GET', 'POST'])
def login():
    return "hello from User login"


@user.route("/logout/", methods=['GET', 'POST'])
def logout():
    return "hello from User logout"
