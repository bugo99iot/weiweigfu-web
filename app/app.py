import os.path
import sys
from pathlib import Path

ROOT_PATH = str(Path(__file__).parent.absolute().parent.absolute())
sys.path.append(ROOT_PATH)

from flask import Flask, render_template
from settings import DEBUG, PORT, HOST

APP_PATH = str(Path(__file__).parent.absolute())
APP_STATIC_PATH = os.path.join(APP_PATH, 'static')
app = Flask(__name__)

app.config.update(APPLICATION_ROOT=APP_PATH,
                  STATIC_FOLDER=APP_STATIC_PATH)


@app.route("/")
def home():
    test_image = os.path.join('static', 'images', 'math_art.jpg')
    return render_template('home.html', test_image=test_image)


if __name__ == "__main__":
    app.run(debug=DEBUG,
            port=PORT,
            host=HOST)
