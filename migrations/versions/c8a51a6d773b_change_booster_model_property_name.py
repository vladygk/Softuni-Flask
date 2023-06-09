"""Change Booster Model property name

Revision ID: c8a51a6d773b
Revises: b205c56b4e1a
Create Date: 2023-04-27 02:04:22.343881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8a51a6d773b'
down_revision = 'b205c56b4e1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('boosters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deck_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('boosters_deck_name_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'decks', ['deck_id'], ['id'])
        batch_op.drop_column('deck_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('boosters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deck_name', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('boosters_deck_name_fkey', 'decks', ['deck_name'], ['id'])
        batch_op.drop_column('deck_id')

    # ### end Alembic commands ###
