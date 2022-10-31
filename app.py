import os.path
import random

from flask import Flask, render_template
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
    return render_template('core/home.html', test_image=test_image)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        print(f"Name:{contact_form.name.data}, "
              f"E-mail:{contact_form.email.data}, "
              f"message:{contact_form.message.data}")
    return render_template("core/contact.html", form=contact_form)


@app.route("/meaning-of-life", methods=["GET"])
def meaning_of_life():
    meaning_of_life_choice: str = random.choice(ProjectData.MEANING_OF_LIFE)
    return render_template('installations/meaning_of_life.html', meaning_of_life=meaning_of_life_choice)


@app.route("/what-do-you-do", methods=["GET"])
def what_do_you_do():
    what_do_you_do_choice: str = random.choice(ProjectData.WHAT_DO_YOU_DO)
    return render_template('installations/what_do_you_do.html', what_do_you_do=what_do_you_do_choice)


if __name__ == "__main__":
    # used locally only for development
    app.run(debug=DEBUG,
            port=5005,
            host='localhost')
