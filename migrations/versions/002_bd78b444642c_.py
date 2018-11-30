"""Add Accessory, Camera and Lense models and relations

Revision ID: bd78b444642c
Revises: 64ff70464028
Create Date: 2018-11-30 08:15:31.171525

"""

# revision identifiers, used by Alembic.
revision = "bd78b444642c"
down_revision = "64ff70464028"

from alembic import op  # noqa: E402
import sqlalchemy as sa  # noqa: E402
import sqlalchemy_utils  # noqa: E402


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "accessory",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("state", sa.Integer(), nullable=False),
        sa.Column("notes", sa.String(length=255), nullable=True),
        sa.Column("manufacturer", sa.String(length=255), nullable=True),
        sa.Column("model", sa.String(length=255), nullable=True),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("extra_notes", sa.Text(), nullable=True),
        sa.Column("serial", sa.String(length=255), nullable=True),
        sa.Column("mount", sa.String(length=255), nullable=True),
        sa.Column("url1", sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column("url2", sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column("url3", sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "camera",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("state", sa.Integer(), nullable=False),
        sa.Column("notes", sa.String(length=255), nullable=True),
        sa.Column("manufacturer", sa.String(length=255), nullable=True),
        sa.Column("model", sa.String(length=255), nullable=True),
        sa.Column("extra_notes", sa.Text(), nullable=True),
        sa.Column("serial", sa.String(length=255), nullable=True),
        sa.Column("mount", sa.String(length=255), nullable=True),
        sa.Column("camera_type", sa.Integer(), nullable=False),
        sa.Column("film_type", sa.Integer(), nullable=False),
        sa.Column("auto_expo", sa.Boolean(), nullable=True),
        sa.Column("auto_focus", sa.Boolean(), nullable=True),
        sa.Column("batteries", sa.String(length=255), nullable=True),
        sa.Column("hot_shoe", sa.Boolean(), nullable=True),
        sa.Column("fixed_lense", sa.Boolean(), nullable=True),
        sa.Column("iso_min", sa.Integer(), nullable=True),
        sa.Column("iso_max", sa.Integer(), nullable=True),
        sa.Column("focale", sa.Integer(), nullable=False),
        sa.Column("min_aperture", sa.Float(), nullable=True),
        sa.Column("max_aperture", sa.Float(), nullable=True),
        sa.Column("blades", sa.Boolean(), nullable=True),
        sa.Column("filter_diameter", sa.Integer(), nullable=False),
        sa.Column("weight", sa.Integer(), nullable=True),
        sa.Column("length", sa.Integer(), nullable=True),
        sa.Column("focus", sa.Integer(), nullable=False),
        sa.Column("focus_length", sa.Integer(), nullable=False),
        sa.Column("macro", sa.Boolean(), nullable=True),
        sa.Column("macro_length", sa.Integer(), nullable=False),
        sa.Column("url1", sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column("url2", sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column("url3", sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "lense",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("state", sa.Integer(), nullable=False),
        sa.Column("notes", sa.String(length=255), nullable=True),
        sa.Column("manufacturer", sa.String(length=255), nullable=True),
        sa.Column("model", sa.String(length=255), nullable=True),
        sa.Column("extra_notes", sa.Text(), nullable=True),
        sa.Column("serial", sa.String(length=255), nullable=True),
        sa.Column("mount", sa.String(length=255), nullable=True),
        sa.Column("focale", sa.Integer(), nullable=False),
        sa.Column("min_aperture", sa.Float(), nullable=True),
        sa.Column("max_aperture", sa.Float(), nullable=True),
        sa.Column("lense_type", sa.Integer(), nullable=False),
        sa.Column("macro", sa.Boolean(), nullable=True),
        sa.Column("macro_length", sa.Integer(), nullable=False),
        sa.Column("filter_diameter", sa.Integer(), nullable=False),
        sa.Column("blades", sa.Boolean(), nullable=True),
        sa.Column("angle", sa.Float(), nullable=True),
        sa.Column("focus", sa.Integer(), nullable=False),
        sa.Column("focus_length", sa.Integer(), nullable=False),
        sa.Column("weight", sa.Integer(), nullable=False),
        sa.Column("length", sa.Integer(), nullable=False),
        sa.Column("url1", sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column("url2", sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column("url3", sqlalchemy_utils.types.url.URLType(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("lense")
    op.drop_table("camera")
    op.drop_table("accessory")
    # ### end Alembic commands ###