from flask import Flask, render_template, redirect, request
from flask_login import LoginManager
from data.forms import Test, Test2
from data.user import User
from user.user import user
from session import db_session
import random
import config
import os

let = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
ALLOWED_EXTENSIONS = ['pdf', 'png', 'jpg', 'jpeg', 'svg']

app = Flask(__name__)
app.config.from_object(config)
login_manager = LoginManager()
login_manager.init_app(app)


def create_random_name(name_len):
    return ''.join([random.choice(let) for i in range(name_len)])


def delete_img(filename):
    for image_format in app.config['SUPPORTED_FORMATS']:
        if filename != "" and os.path.exists(f"{app.config['UPLOAD_FOLDER']}{filename}.{image_format}"):
            os.remove(f"{app.config['UPLOAD_FOLDER']}{filename}.{image_format}")


def clear_folder(folder_name, path=app.config['UPLOAD_FOLDER']):
    delete_folder(folder_name, path=path)
    os.makedirs(path+folder_name)


def delete_folder(folder_name, path=app.config['UPLOAD_FOLDER']):
    if os.path.exists(path+folder_name):
        for filename in os.listdir(path + folder_name):
            if os.path.isdir(f"{path}{folder_name}/{filename}"):
                delete_folder(f"{folder_name}/{filename}")
            else:
                os.remove(f"{path}{folder_name}/{filename}")
        os.rmdir(path+folder_name)


def get_files_from(folder, path=app.config["UPLOAD_FOLDER"], add_path=None):
    files = []
    if os.path.exists(path+folder):
        files = os.listdir(path+folder)
    files = [(folder+"/"+f) if not add_path else ("/"+add_path+folder+"/"+f) for f in files]
    print(files)
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
        files = request.files
        clear_folder("for_test")
        for ind, key in enumerate(dict(files).keys()):
            if files[key].filename != "" and files[key].filename.split(".")[-1] in ALLOWED_EXTENSIONS:
                files[key].save(f'{app.config["UPLOAD_FOLDER"]}{upload_folder}/{ind}{create_random_name(50)}.{files[key].filename.split(".")[-1]}')
    return render_template("test.html", form=form, error=error, form_title="Test page", filenames=get_files_from("for_test", add_path=app.config["UPLOAD_FOLDER"]))


@app.route("/test2/", methods=['GET', 'POST'])
def test2():
    form = Test2()
    error = "Error"
    return render_template("test2.html", form=form, error=error, form_title="Test page")


@app.route("/")
def main_page():
    return redirect('/test')


app.register_blueprint(user, url_prefix="/user")

if __name__ == '__main__':
    app.run()
