from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField(label='Name', render_kw={'class': 'contact_stringfield'}, validators=[DataRequired()])
    email = StringField(label='Email', render_kw={'class': 'contact_stringfield'}, validators=[DataRequired(), Email()])
    message = TextAreaField(label='Message', render_kw={'class': 'contact_textareafield'}, validators=[DataRequired()])
    send = SubmitField(label="Send")
