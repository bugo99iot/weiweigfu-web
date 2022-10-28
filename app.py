import os.path
from pathlib import Path

from flask import Flask, render_template
from settings import DEBUG, FLASK_APP_SECRET_KEY

from forms import ContactForm

APP_PATH = str(Path(__file__).parent.absolute())
APP_STATIC_PATH = os.path.join(APP_PATH, 'static')
app = Flask(__name__)

app.config.update(APPLICATION_ROOT=APP_PATH,
                  STATIC_FOLDER=APP_STATIC_PATH,
                  SECRET_KEY=FLASK_APP_SECRET_KEY)


@app.route("/")
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


if __name__ == "__main__":
    # used locally only for development
    app.run(debug=DEBUG,
            port=5005,
            host='localhost')
