import datetime

from flask_security import SQLAlchemyUserDatastore, UserMixin, RoleMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.ext.hybrid import Comparator
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import func
from sqlalchemy_searchable import make_searchable
from sqlalchemy_utils.types.url import URLType

db = SQLAlchemy()
make_searchable(db.metadata)


# #### Base ####


class CaseInsensitiveComparator(Comparator):
    def __eq__(self, other):
        return func.lower(self.__clause_element__()) == func.lower(other)


class Config(db.Model):
    __tablename__ = "config"

    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(255), default=None)
    app_description = db.Column(db.Text)


# #### User ####

roles_users = db.Table(
    "roles_users",
    db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
    db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, info={"label": "Name"})
    description = db.Column(db.String(255), info={"label": "Description"})

    __mapper_args__ = {"order_by": name}


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, info={"label": "Email"})
    name = db.Column(db.String(255), unique=True, nullable=False, info={"label": "Username"})
    password = db.Column(db.String(255), nullable=False, info={"label": "Password"})
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    display_name = db.Column(db.String(30), nullable=True, info={"label": "Display name"})

    locale = db.Column(db.String(5), default="en")

    timezone = db.Column(db.String(255), nullable=False, default="UTC")  # Managed and fed by pytz

    slug = db.Column(db.String(255), unique=True, nullable=True)

    roles = db.relationship("Role", secondary=roles_users, backref=db.backref("users", lazy="dynamic"))

    user_loggings = db.relationship("UserLogging", backref="user", lazy="dynamic", cascade="delete")
    loggings = db.relationship("Logging", backref="user", lazy="dynamic", cascade="delete")

    accessories = db.relationship("Accessory", backref="user", lazy="dynamic", cascade="delete")
    lenses = db.relationship("Lense", backref="user", lazy="dynamic", cascade="delete")
    cameras = db.relationship("Camera", backref="user", lazy="dynamic", cascade="delete")

    __mapper_args__ = {"order_by": name}

    def join_roles(self, string):
        return string.join([i.description for i in self.roles])

    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = target.name

    @hybrid_property
    def name_insensitive(self):
        return self.name.lower()

    @name_insensitive.comparator
    def name_insensitive(cls):
        return CaseInsensitiveComparator(cls.name)

    def __repr__(self):
        return f"<User(id='{self.id}', name='{self.name}')>"

    def username(self):
        if not self.display_name:
            return self.name
        elif len(self.display_name) > 0:
            return self.display_name
        else:
            return self.name


event.listen(User.name, "set", User.generate_slug, retval=False)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)


# #### Logging ####


class Logging(db.Model):
    __tablename__ = "logging"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False, default="General")
    level = db.Column(db.String(255), nullable=False, default="INFO")
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(
        db.DateTime(timezone=False), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=True)

    __mapper_args__ = {"order_by": timestamp.desc()}


class UserLogging(db.Model):
    __tablename__ = "user_logging"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False, default="General")
    level = db.Column(db.String(255), nullable=False, default="INFO")
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(
        db.DateTime(timezone=False), default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )
    item_id = db.Column(db.Integer(), nullable=True)

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)

    __mapper_args__ = {"order_by": timestamp.desc()}


enum_states = {
    0: "Unknown",
    5: "Very Good",
    10: "Good",
    15: "Ok, scratches",
    20: "Not so ok",
    25: "Cracks",
    30: "Partly working",
    35: "RIP"
}

ENUM_LENSES_TYPES = [(0, "Unknown"), (5, "Wide Angle"), (10, "Standard"), (15, "Zoom"), (20, "Telephoto")]

ENUM_CAMERAS_TYPES = [
    (0, "Unknown"),
    (5, "Chamber"),
    (10, "Chamber Stereo"),
    (15, "Folding"),
    (20, "Box"),
    (25, "Box Stereo"),
    (30, "Instant"),
    (35, "Disposable"),
    (40, "Toy"),
    (45, "Panoramic"),
    (50, "Reflex SLR"),
    (55, "Reflex TLR"),
    (60, "Reflex DSLR"),
]

ENUM_FILM_TYPES = [
    (0, "Unknown"),
    (5, "8mm"),
    (10, "9.5mm"),
    (15, "16mm"),
    (20, "17.5mm"),
    (25, "28mm"),
    (30, "35mm"),
    (35, "70mm"),
    (40, "110"),
    (45, "120"),
    (50, "126"),
    (55, "127"),
    (60, "135"),
    (65, "616"),
    (70, "628"),
    (75, "Disc"),
    (80, "Ektachrome"),
    (85, "Ektar"),
    (90, "Kodachrome"),
    (95, "Eastmancolor"),
    (100, "Plate"),
    (105, "Pack-Film"),
    (110, "Pack-Film 100"),
    (115, "Pack-Film 100 or 80"),
    (120, "Pack-Film 80"),
]

ENUM_FOCUSES_TYPES = [(0, "Unknown"), (5, "Manual"), (10, "Automatic"), (15, "Fixed")]


class Accessory(db.Model):
    __tablename__ = "accessory"
    id = db.Column(db.Integer, primary_key=True)

    state = db.Column(db.Integer(), nullable=False, default=0)  # ENUM_STATES
    state_notes = db.Column(db.String(255), nullable=True)

    manufacturer = db.Column(db.String(255), nullable=True)
    model = db.Column(db.String(255), nullable=True)
    model_notes = db.Column(db.Text, nullable=True)
    description = db.Column(db.String(255), nullable=True)
    serial = db.Column(db.String(255), nullable=True)
    mount = db.Column(db.String(255), nullable=True)

    private = db.Column(db.Boolean(), default=False)

    url1 = db.Column(URLType(), nullable=True)
    url2 = db.Column(URLType(), nullable=True)
    url3 = db.Column(URLType(), nullable=True)

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)

    def state_str(self):
        return enum_states[self.state]


class Lense(db.Model):
    __tablename__ = "lense"
    id = db.Column(db.Integer, primary_key=True)

    state = db.Column(db.Integer(), nullable=False, default=0)  # ENUM_STATES
    state_notes = db.Column(db.String(255), nullable=True)

    manufacturer = db.Column(db.String(255), nullable=True)
    model = db.Column(db.String(255), nullable=True)
    model_notes = db.Column(db.Text, nullable=True)
    description = db.Column(db.String(255), nullable=True)
    serial = db.Column(db.String(255), nullable=True)
    mount = db.Column(db.String(255), nullable=True)

    focale = db.Column(db.Integer(), nullable=False, default=0)
    min_aperture = db.Column(db.Float(), default=0)
    max_aperture = db.Column(db.Float(), default=0)
    lense_type = db.Column(db.Integer(), nullable=False, default=0)  # ENUM_LENSES_TYPES
    macro = db.Column(db.Boolean(), default=True)
    macro_length = db.Column(db.Integer(), nullable=False, default=0)
    filter_diameter = db.Column(db.Integer(), nullable=False, default=0)
    blades = db.Column(db.Boolean(), default=True)
    angle = db.Column(db.Float(), default=0)
    focus = db.Column(db.Integer(), nullable=False, default=0)  # ENUM_FOCUSES_TYPES
    focus_length = db.Column(db.Integer(), nullable=False, default=0)
    weight = db.Column(db.Integer(), nullable=False, default=0)  # g.
    length = db.Column(db.Float(), nullable=False, default=0)  # mm

    private = db.Column(db.Boolean(), default=False)

    url1 = db.Column(URLType(), nullable=True)
    url2 = db.Column(URLType(), nullable=True)
    url3 = db.Column(URLType(), nullable=True)

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)

    def state_str(self):
        return enum_states[self.state]


class Camera(db.Model):
    __tablename__ = "camera"
    id = db.Column(db.Integer, primary_key=True)

    state = db.Column(db.Integer(), nullable=False, default=0)  # ENUM_STATES
    state_notes = db.Column(db.String(255), nullable=True)

    manufacturer = db.Column(db.String(255), nullable=True)
    model = db.Column(db.String(255), nullable=True)
    model_notes = db.Column(db.Text, nullable=True)
    description = db.Column(db.String(255), nullable=True)
    serial = db.Column(db.String(255), nullable=True)
    mount = db.Column(db.String(255), nullable=True)

    camera_type = db.Column(db.Integer(), nullable=False, default=0)  # ENUM_CAMERAS_TYPES

    film_type = db.Column(db.Integer(), nullable=False, default=0)  # ENUM_FILM_TYPES
    auto_expo = db.Column(db.Boolean(), default=True)
    auto_focus = db.Column(db.Boolean(), default=True)
    batteries = db.Column(db.String(255), nullable=True)
    hot_shoe = db.Column(db.Boolean(), default=True)
    fixed_lense = db.Column(db.Boolean(), default=False)

    iso_min = db.Column(db.Integer(), default=0)
    iso_max = db.Column(db.Integer(), default=0)
    focale = db.Column(db.Integer(), nullable=False, default=0)
    min_aperture = db.Column(db.Float(), default=0)
    max_aperture = db.Column(db.Float(), default=0)
    blades = db.Column(db.Boolean(), default=True)
    filter_diameter = db.Column(db.Integer(), nullable=False, default=0)
    weight = db.Column(db.Integer(), nullable=True, default=0)  # g.
    length = db.Column(db.Integer(), nullable=True, default=0)  # mm
    focus = db.Column(db.Integer(), nullable=False, default=0)  # ENUM_FOCUSES_TYPES
    focus_length = db.Column(db.Integer(), nullable=False, default=0)
    macro = db.Column(db.Boolean(), default=True)
    macro_length = db.Column(db.Integer(), nullable=False, default=0)

    private = db.Column(db.Boolean(), default=False)

    url1 = db.Column(URLType(), nullable=True)
    url2 = db.Column(URLType(), nullable=True)
    url3 = db.Column(URLType(), nullable=True)

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)

    def state_str(self):
        return enum_states[self.state]
