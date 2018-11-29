import datetime
import os

from flask_security import SQLAlchemyUserDatastore, UserMixin, RoleMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.ext.hybrid import Comparator
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import func
from sqlalchemy_searchable import make_searchable

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
