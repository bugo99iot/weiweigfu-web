import os.path
import random

from flask import Flask, render_template
from flask import request

from settings import DEBUG
from settings import FLASK_APP_SECRET_KEY
from settings import APP_PATH, APP_STATIC_PATH
from utils.load_data import ProjectData

from utils.forms import ContactForm

app = Flask(__name__)

app.config.update(APPLICATION_ROOT=APP_PATH,
                  STATIC_FOLDER=APP_STATIC_PATH,
                  SECRET_KEY=FLASK_APP_SECRET_KEY)


@app.route("/", methods=["GET"])
def home():
    test_image = os.path.join('static', 'images', 'math_art.jpg')
    return render_template('core/home.html', test_image=test_image, title='WeiWeiGFU')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print(f"Name:{form.name.data}, E-mail:{form.email.data}, message: {form.message.data}")

    return render_template("core/contact.html", form=form)


@app.route("/meaning-of-life", methods=["GET"])
def meaning_of_life():
    meaning_of_life_choice: str = random.choice(ProjectData.MEANING_OF_LIFE)
    return render_template('installations/meaning_of_life.html',
                           title='Meaning of Life',
                           meaning_of_life=meaning_of_life_choice)


@app.route("/what-do-you-do", methods=["GET"])
def what_do_you_do():
    what_do_you_do_choice: str = random.choice(ProjectData.WHAT_DO_YOU_DO)
    return render_template('installations/what_do_you_do.html',
                           title='What do you do',
                           what_do_you_do=what_do_you_do_choice)


@app.route("/child", methods=["GET"])
def child():
    return render_template('test/child.html',
                           title='Child',
                           description="Smarter page templates with Flask & Jinja.")


if __name__ == "__main__":
    # used locally only for development
    app.run(debug=DEBUG,
            port=5005,
            host='localhost')
