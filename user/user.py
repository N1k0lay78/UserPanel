from flask import Blueprint, render_template, request, redirect
from data.forms import FormRegister
from data.Api.Inner.InnerAdmin import get_user, put_user, get_list_user, create_new_user, user_check_password

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
        res = create_new_user({"fullname": form.fullname.data, "nickname": form.nickname.data, "email": form.email.data,
                               "password_1": form.password_1.data, "password_2": form.password_2.data})
        if "success" in res:
            return redirect("/user/login")
        else:
            error = res["error"]

    return render_template("register.html", form=form, error=error, form_title="Регистрация")


@user.route("/login/", methods=['GET', 'POST'])
def login():
    form = FormRegister()
    error = ""
    if request.method == "POST":
        res = user_check_password(form.email.data, form.password_1.data)
        if "success" in res:
            return redirect("/")
        if "error" in res:
            error = res["error"]
    return render_template("login.html", form=form, error=error, form_title="Логин")


@user.route("/logout/", methods=['GET', 'POST'])
def logout():
    return "hello from User logout"
