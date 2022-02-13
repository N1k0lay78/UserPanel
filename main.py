from flask import Flask, render_template, redirect
from flask_login import LoginManager

from data.forms import Test, Test2
from data.user import User
from user.user import user
from session import db_session
import config

app = Flask(__name__)
app.config.from_object(config)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    session.close()
    return user


@app.errorhandler(404)
def not_found(error):
    return "ups don't nashel", 404


@app.errorhandler(500)
def inner_error(error):
    return "ups server upal, ego vetrom sdulo", 500


@app.route("/favicon.ico", methods=['GET', 'POST'])
def favicon():
    return redirect("/static/img/favicon.svg")


@app.route("/test/", methods=['GET', 'POST'])
def test():
    form = Test()
    error = "Error"
    return render_template("test.html", form=form, error=error, form_title="Test page")


@app.route("/test2/", methods=['GET', 'POST'])
def test2():
    form = Test2()
    error = "Error"
    return render_template("test2.html", form=form, error=error, form_title="Test page")


app.register_blueprint(user, url_prefix="/user")

if __name__ == '__main__':
    app.run()
