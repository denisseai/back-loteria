"""creates initial tables

Revision ID: d184ebee91cb
Revises: 
Create Date: 2021-07-22 11:44:39.422263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd184ebee91cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deck',
    sa.Column('deck_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('deck_id')
    )
    op.create_table('player',
    sa.Column('player_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('win_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('player_id')
    )
    op.create_table('card',
    sa.Column('card_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('deck_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['deck_id'], ['deck.deck_id'], ),
    sa.PrimaryKeyConstraint('card_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('card')
    op.drop_table('player')
    op.drop_table('deck')
    # ### end Alembic commands ###
