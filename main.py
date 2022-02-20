import os
from flask import Flask, render_template, redirect, request
from flask_login import LoginManager
from data.forms import Test, Test2
from data.user import User
from user.user import user
from session import db_session
import config
from PIL import Image
from wtforms.fields.simple import FileField

app = Flask(__name__)
app.config.from_object(config)
login_manager = LoginManager()
login_manager.init_app(app)


def delete_img(filename):
    for image_format in app.config['SUPPORTED_FORMATS']:
        if filename != "" and os.path.exists(f"{app.config['UPLOAD_FOLDER']}{filename}.{image_format}"):
            os.remove(f"{app.config['UPLOAD_FOLDER']}{filename}.{image_format}")


def get_files_from(folder, path=app.config["UPLOAD_FOLDER"]):
    files = []
    if os.path.exists(path+folder):
        files = os.listdir(path+folder)
    files = [folder+"/"+f for f in files]
    return files


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
    upload_folder = "for_test"
    if request.method == "POST":
        for i in range(1, 21):
            inf = form[f"image_{i}"].data
            # print(form[f"image_{i}"])
            if inf.filename != "":
                if inf.filename.split(".")[-1] in app.config['SUPPORTED_FORMATS']:
                    print(form[f"image_{i}"])
                    print(type(form[f"image_{i}"]))
                    delete_img(f"{upload_folder}/{inf.name}")
                    inf.save(f'{app.config["UPLOAD_FOLDER"]}{upload_folder}/{inf.name}.{inf.filename.split(".")[-1]}')
            else:
                delete_img(f"{upload_folder}/{inf.name}")
    filenames = {}
    for i, filename in enumerate(get_files_from("for_test"), start=1):
        filenames[f"image_{i}"] = "/" + app.config["UPLOAD_FOLDER"] + filename

    return render_template("test.html", form=form, error=error, form_title="Test page", filenames=filenames)


@app.route("/test2/", methods=['GET', 'POST'])
def test2():
    form = Test2()
    error = "Error"
    return render_template("test2.html", form=form, error=error, form_title="Test page")


app.register_blueprint(user, url_prefix="/user")

if __name__ == '__main__':
    app.run()
