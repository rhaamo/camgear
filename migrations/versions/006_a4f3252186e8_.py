"""Add picture filename

Revision ID: a4f3252186e8
Revises: a5506eaab316
Create Date: 2018-11-30 17:01:59.352042

"""

# revision identifiers, used by Alembic.
revision = "a4f3252186e8"
down_revision = "a5506eaab316"

from alembic import op  # noqa: E402
import sqlalchemy as sa  # noqa: E402


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("accessory", schema=None) as batch_op:
        batch_op.add_column(sa.Column("pic_filename", sa.String(length=255), nullable=True))

    with op.batch_alter_table("camera", schema=None) as batch_op:
        batch_op.add_column(sa.Column("pic_filename", sa.String(length=255), nullable=True))

    with op.batch_alter_table("lense", schema=None) as batch_op:
        batch_op.add_column(sa.Column("pic_filename", sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("lense", schema=None) as batch_op:
        batch_op.drop_column("pic_filename")

    with op.batch_alter_table("camera", schema=None) as batch_op:
        batch_op.drop_column("pic_filename")

    with op.batch_alter_table("accessory", schema=None) as batch_op:
        batch_op.drop_column("pic_filename")

    # ### end Alembic commands ###
