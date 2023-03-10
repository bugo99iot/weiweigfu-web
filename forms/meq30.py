from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

meq30_score_choices = [(None, 'Select'),
                       (0, 'None'),
                       (1, 'Can\'t decide'),
                       (2, 'Slight'),
                       (3, 'Moderate'),
                       (4, 'Strong'),
                       (5, 'Extreme')]

substance_choice = [(None, 'Select'),
                    ('lsd', 'LSD'),
                    ('psilocybin', 'Psilocybin / Mushrooms or Truffles'),
                    ('5-meo-dmt', '5-Meo-DMT (synthetic)'),
                    ('bufo', 'Bufo / Toad'),
                    ('dmt', 'DMT (synthetic)'),
                    ('ayahuasca', 'Ayahuasca'),
                    ('mescaline', 'Mescaline (synthetic)'),
                    ('san_pedro', 'San Pedro'),
                    ('peyote', 'Peyote'),
                    ('ibogaine', 'Ibogaine'),
                    ('ketamine', 'Ketamine'),
                    ('other', 'Other'),
                    ('dont_know', 'Don\'t know'),
                    ('dont_want_say', 'Don\'t want to say')]


class Meq30Form(FlaskForm):
    substance = SelectField(label='Hallucinogen in use',
                            choices=substance_choice)

    # Factor 1: Mystical

    q1 = SelectField(label='Feeling that you experienced eternity or infinity.',
                     choices=meq30_score_choices,
                     validators=[DataRequired()],
                     default=None)

    q2 = SelectField(label='Freedom from the limitations of your personal self and feeling a unity or bond with '
                           'what was felt to be greater than your personal self.',
                     choices=meq30_score_choices,
                     validators=[DataRequired()],
                     default=None)

    q7 = SelectField(label='Experience of oneness or unity with objects and/or persons perceived in your surroundings.',
                     choices=meq30_score_choices,
                     validators=[DataRequired()],
                     default=None)

    q10 = SelectField(label='Gain of insightful knowledge experienced at an intuitive level.',
                      choices=meq30_score_choices,
                      validators=[DataRequired()],
                      default=None)

    q13 = SelectField(label='Sense of being at a spiritual height.',
                      choices=meq30_score_choices,
                      validators=[DataRequired()],
                      default=None)

    # Factor 2: Positive Mood

    q16 = SelectField(label='Experience of amazement.',
                      choices=meq30_score_choices,
                      validators=[DataRequired()],
                      default=None)

    # Factor 3: Transcendence of Time and Space

    q22 = SelectField(label='Loss of your usual sense of time.',
                      choices=meq30_score_choices,
                      validators=[DataRequired()],
                      default=None)

    # Factor 4: Ineffability

    q28 = SelectField(label='Sense that the experience cannot be described adequately in words.',
                      choices=meq30_score_choices,
                      validators=[DataRequired()],
                      default=None)

    # get score
    get_score = SubmitField(label="Get score")

    def calculate_score(self):
        return
