"""Add User model

Revision ID: 1de5123acd21
Revises: 973e3bfe2774
Create Date: 2023-09-01 17:22:27.298860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1de5123acd21'
down_revision = '973e3bfe2774'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game_users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('game_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name='fk_game_users_game_id_games'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_game_users_user_id_users'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
