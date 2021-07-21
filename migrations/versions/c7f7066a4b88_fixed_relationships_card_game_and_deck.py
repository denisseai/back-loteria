"""fixed relationships card, game and deck

Revision ID: c7f7066a4b88
Revises: 86c89b00859d
Create Date: 2021-07-20 14:45:55.174656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7f7066a4b88'
down_revision = '86c89b00859d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('deck_game_id_fkey', 'deck', type_='foreignkey')
    op.drop_column('deck', 'game_id')
    op.add_column('game', sa.Column('deck_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'game', 'deck', ['deck_id'], ['deck_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'game', type_='foreignkey')
    op.drop_column('game', 'deck_id')
    op.add_column('deck', sa.Column('game_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('deck_game_id_fkey', 'deck', 'game', ['game_id'], ['game_id'])
    # ### end Alembic commands ###