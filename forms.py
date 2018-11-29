from flask_security import RegisterForm
from flask_uploads import UploadSet, AUDIO
from flask_wtf import FlaskForm as Form
from wtforms import PasswordField, SubmitField, SelectField
from wtforms import widgets
from wtforms.fields.core import StringField
from wtforms.validators import DataRequired, ValidationError, Length, Regexp
from wtforms_alchemy import model_form_factory
from flask_babelex import gettext

from models import db, User

BaseModelForm = model_form_factory(Form)

sounds = UploadSet("sounds", AUDIO)


class PasswordFieldNotHidden(StringField):
    """
    Original source: https://github.com/wtforms/wtforms/blob/2.0.2/wtforms/fields/simple.py#L35-L42  # noqa: E501

    A StringField, except renders an ``<input type="password">``.
    Also, whatever value is accepted by this field is not rendered back
    to the browser like normal fields.
    """

    widget = widgets.PasswordInput(hide_value=False)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(cls):
        return db.session


class ExtendedRegisterForm(RegisterForm):
    name = StringField("Username", [DataRequired(), Regexp(regex=r"^\w+$"), Length(max=150)])

    def validate_name(form, field):
        if len(field.data) <= 0:
            raise ValidationError(gettext("Username required"))

        u = db.session.query(User).filter_by(name_insensitive=field.data).first()
        if u:
            raise ValidationError(gettext("Username already taken"))


class UserProfileForm(BaseModelForm):

    password = PasswordField(gettext("Password"), [Length(max=255)])
    name = StringField(gettext("Name"), [Length(max=255)])
    display_name = StringField(gettext("Display name"), [Length(max=30)])
    email = StringField(gettext("Email"), [Length(max=255)])
    timezone = SelectField(coerce=str, label=gettext("Timezone"), default="UTC")
    locale = SelectField(gettext("Locale"), default="en", choices=[["en", "English"], ["fr", "French"]])
    submit = SubmitField(gettext("Update profile"))
