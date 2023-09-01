"""Add game_user Association Table

Revision ID: 2140a06d3267
Revises: 1de5123acd21
Create Date: 2023-09-01 17:35:28.221660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2140a06d3267'
down_revision = '1de5123acd21'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_users',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_game_users_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_game_users_user_id_users')),
    sa.PrimaryKeyConstraint('game_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_users')
    # ### end Alembic commands ###
