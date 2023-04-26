"""Add attribute filed to Card model

Revision ID: 345701ecb099
Revises: eed1cae4448c
Create Date: 2023-04-26 21:40:38.219570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '345701ecb099'
down_revision = 'eed1cae4448c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.add_column(sa.Column('attribute', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cards', schema=None) as batch_op:
        batch_op.drop_column('attribute')

    # ### end Alembic commands ###