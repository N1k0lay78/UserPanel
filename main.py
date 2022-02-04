from flask import Flask
from flask_login import LoginManager
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


app.register_blueprint(user, url_prefix="/user")

if __name__ == '__main__':
    app.run()
