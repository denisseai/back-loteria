"""empty message

Revision ID: 950702b6f1c4
Revises: 
Create Date: 2021-07-20 11:41:01.921423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '950702b6f1c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('game_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('game_id')
    )
    op.create_table('player',
    sa.Column('player_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('player_id')
    )
    op.create_table('card',
    sa.Column('card_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('img', sa.String(), nullable=True),
    sa.Column('deck_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['deck_id'], ['game.game_id'], ),
    sa.PrimaryKeyConstraint('card_id')
    )
    op.create_table('deck',
    sa.Column('deck_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['game.game_id'], ),
    sa.PrimaryKeyConstraint('deck_id')
    )
    op.create_table('game_player',
    sa.Column('game_player_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('win_count', sa.Integer(), nullable=True),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['game.game_id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['player.player_id'], ),
    sa.PrimaryKeyConstraint('game_player_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_player')
    op.drop_table('deck')
    op.drop_table('card')
    op.drop_table('player')
    op.drop_table('game')
    # ### end Alembic commands ###