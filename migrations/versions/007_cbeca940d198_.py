"""Fix lens typo

Revision ID: cbeca940d198
Revises: a4f3252186e8
Create Date: 2018-11-30 19:38:19.747054

"""

# revision identifiers, used by Alembic.
revision = "cbeca940d198"
down_revision = "a4f3252186e8"

from alembic import op  # noqa: E402
import sqlalchemy as sa  # noqa: E402


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("camera", schema=None) as batch_op:
        batch_op.add_column(sa.Column("fixed_lens", sa.Boolean(), nullable=True))
        batch_op.drop_column("fixed_lense")

    with op.batch_alter_table("lense", schema=None) as batch_op:
        batch_op.add_column(sa.Column("lens_type", sa.Integer(), nullable=False, default=0))
        batch_op.drop_column("lense_type")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("lense", schema=None) as batch_op:
        batch_op.add_column(sa.Column("lense_type", sa.INTEGER(), nullable=False, default=0))
        batch_op.drop_column("lens_type")

    with op.batch_alter_table("camera", schema=None) as batch_op:
        batch_op.add_column(sa.Column("fixed_lense", sa.BOOLEAN(), nullable=True))
        batch_op.drop_column("fixed_lens")

    # ### end Alembic commands ###
