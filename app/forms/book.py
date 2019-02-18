from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30), DataRequired()])
    page = IntegerField(validators=[NumberRange(min=1, max=999)], default=1)
