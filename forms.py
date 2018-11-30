from flask_security import RegisterForm
from flask_uploads import UploadSet, AUDIO
from flask_wtf import FlaskForm as Form
from wtforms import PasswordField, SubmitField, SelectField, TextAreaField
from wtforms import widgets
from wtforms.fields.core import StringField, IntegerField, BooleanField, FloatField
from wtforms.validators import DataRequired, ValidationError, Length, Regexp
from wtforms_alchemy import model_form_factory
from flask_babelex import gettext

from models import db, User, ENUM_CAMERAS_TYPES, ENUM_FILM_TYPES, ENUM_FOCUSES_TYPES, ENUM_LENSES_TYPES, ENUM_STATES

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


class AccessoryForm(BaseModelForm):
    state = SelectField(coerce=int, label=gettext("State"), choices=ENUM_STATES, default=0)
    state_notes = StringField(gettext("State notes"), [Length(max=255)])

    manufacturer = StringField(gettext("Manufacturer"), [Length(max=255)])
    model = StringField(gettext("Model"), [Length(max=255)])
    model_notes = TextAreaField(gettext("Model notes"))
    description = TextAreaField(gettext("Description"))
    serial = StringField(gettext("Serial number"), [Length(max=255)])
    mount = StringField(gettext("Mount"), [Length(max=255)])

    url1 = StringField(gettext("URL 1"), [Length(max=255)])
    url2 = StringField(gettext("URL 2"), [Length(max=255)])
    url3 = StringField(gettext("URL 3"), [Length(max=255)])


class AccessoryAddForm(AccessoryForm):
    submit = SubmitField(gettext("Add Accessory"))


class AccessoryEditForm(AccessoryForm):
    submit = SubmitField(gettext("Update Accessory"))


class LenseForm(BaseModelForm):
    state = SelectField(coerce=int, label=gettext("State"), choices=ENUM_STATES, default=0)
    state_notes = StringField(gettext("State notes"), [Length(max=255)])

    manufacturer = StringField(gettext("Manufacturer"), [Length(max=255)])
    model = StringField(gettext("Model"), [Length(max=255)])
    model_notes = TextAreaField(gettext("Model notes"))
    description = TextAreaField(gettext("Description"))
    serial = StringField(gettext("Serial number"), [Length(max=255)])
    mount = StringField(gettext("Mount"), [Length(max=255)])

    focale = IntegerField(gettext("Focale"), default=0)
    min_aperture = FloatField(gettext("Min Aperture"))
    max_aperture = FloatField(gettext("Max Aperture"))
    lense_type = SelectField(coerce=int, label=gettext("Lense Type"), choices=ENUM_LENSES_TYPES, default=0)
    macro = BooleanField(gettext("Macro capable"))
    macro_length = IntegerField(gettext("Min distance for macro (cm)"))
    filter_diameter = IntegerField(gettext("Filter Diameter (mm)"))
    blades = BooleanField(gettext("Using blades"))
    angle = FloatField(gettext("View angle (°)"))
    focus = SelectField(coerce=int, label=gettext("Focus Mode"), choices=ENUM_FOCUSES_TYPES, default=0)
    focus_length = IntegerField(gettext("Min distance for focus (cm)"))
    weight = IntegerField(gettext("Weight (g)"))
    length = FloatField(gettext("Length (cm)"))

    url1 = StringField(gettext("URL 1"), [Length(max=255)])
    url2 = StringField(gettext("URL 2"), [Length(max=255)])
    url3 = StringField(gettext("URL 3"), [Length(max=255)])


class LenseAddForm(LenseForm):
    submit = SubmitField(gettext("Add Lense"))


class LenseEditForm(LenseForm):
    submit = SubmitField(gettext("Update Lense"))


class CameraForm(BaseModelForm):
    state = SelectField(coerce=int, label=gettext("State"), choices=ENUM_STATES, default=0)
    state_notes = StringField(gettext("State notes"), [Length(max=255)])

    manufacturer = StringField(gettext("Manufacturer"), [Length(max=255)])
    model = StringField(gettext("Model"), [Length(max=255)])
    model_notes = TextAreaField(gettext("Model notes"))
    description = TextAreaField(gettext("Description"))
    serial = StringField(gettext("Serial number"), [Length(max=255)])
    mount = StringField(gettext("Mount"), [Length(max=255)])

    camera_type = SelectField(coerce=int, label=gettext("Camera Type"), choices=ENUM_CAMERAS_TYPES, default=0)

    film_type = SelectField(coerce=int, label=gettext("Film Type"), choices=ENUM_FILM_TYPES, default=0)
    auto_expo = BooleanField(gettext("Auto exposure"))
    auto_focus = BooleanField(gettext("Auto focus"))
    batteries = StringField(gettext("Batteries type"))
    hot_shoe = BooleanField(gettext("Hot Shoe"))
    fixed_lense = BooleanField(gettext("Fixed lense"))

    iso_min = IntegerField(gettext("ISO Min"))
    iso_max = IntegerField(gettext("ISO Max"))
    focale = IntegerField(gettext("Focale"))
    min_aperture = FloatField(gettext("Min Aperture"))
    max_aperture = FloatField(gettext("Max Aperture"))
    blades = BooleanField(gettext("Using blades"))
    filter_diameter = IntegerField(gettext("Filter Diameter (mm)"))
    focus = SelectField(coerce=int, label=gettext("Focus Mode"), choices=ENUM_FOCUSES_TYPES, default=0)
    focus_length = IntegerField(gettext("Min distance for focus (cm)"))
    macro = BooleanField(gettext("Macro capable"))
    macro_length = IntegerField(gettext("Min distance for macro (cm)"))
    weight = IntegerField(gettext("Weight (g)"))
    length = FloatField(gettext("Length (cm)"))

    url1 = StringField(gettext("URL 1"), [Length(max=255)])
    url2 = StringField(gettext("URL 2"), [Length(max=255)])
    url3 = StringField(gettext("URL 3"), [Length(max=255)])


class CameraAddForm(CameraForm):
    submit = SubmitField(gettext("Add Camera"))


class CameraEditForm(CameraForm):
    submit = SubmitField(gettext("Update Camera"))
