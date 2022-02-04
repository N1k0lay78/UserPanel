from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, current_user, login_required, logout_user
from data.forms import FormRegister, FormLogin
from data.Api.Inner.InnerAdmin import get_user, put_user, get_list_user, create_new_user, user_check_password
from data.user import User
from session import db_session

user = Blueprint('user', __name__, template_folder="pages")


@user.route("/")
def main():
    return render_template("test.html")


@user.route("/register/", methods=['GET', 'POST'])
def register():
    if not current_user.is_anonymous:
        return redirect("/")

    form = FormRegister()
    error = ""
    if request.method == 'POST':
        res = create_new_user({"fullname": form.fullname.data, "nickname": form.nickname.data, "email": form.email.data,
                               "password_1": form.password_1.data, "password_2": form.password_2.data})
        if "success" in res:
            return redirect("/user/login")
        else:
            print(res)
            error = res["error"]

    return render_template("register.html", form=form, error=error, form_title="Регистрация")


@user.route("/login/", methods=['GET', 'POST'])
def login():
    form = FormLogin()
    error = ""
    if not current_user.is_anonymous:
        return redirect("/")
    if request.method == "POST":
        res = user_check_password(form.email.data, form.password.data)
        if "success" in res:
            session = db_session.create_session()
            user = session.query(User).filter(User.id == int(res["id"])).first()
            login_user(user, remember=form.remember.data)
            session.close()
            return redirect("/")
        if "error" in res:
            error = res["error"]
    return render_template("login.html", form=form, error=error, form_title="Логин")


@user.route("/logout/", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect("/")
