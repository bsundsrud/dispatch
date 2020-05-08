"""Adds after_hours_notification column to Participant model

Revision ID: d1e66a4ef671
Revises: 9a3478cbe76c
Create Date: 2020-05-03 20:41:43.402097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d1e66a4ef671"
down_revision = "9a3478cbe76c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("participant", sa.Column("after_hours_notification", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("participant", "after_hours_notification")
    # ### end Alembic commands ###
