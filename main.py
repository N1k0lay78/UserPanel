from flask import Flask
from user.user import user
import config

app = Flask(__name__)
app.config.from_object(config)


@app.errorhandler(404)
def not_found(error):
    return "ups don't nashel", 404


@app.errorhandler(500)
def not_found(error):
    return "ups server upal, ego vetrom sdulo", 500


app.register_blueprint(user, url_prefix="/user", set_folder="")

if __name__ == '__main__':
    app.run()
