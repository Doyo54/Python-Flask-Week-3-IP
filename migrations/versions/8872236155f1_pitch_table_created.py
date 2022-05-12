"""Pitch table created

Revision ID: 8872236155f1
Revises: 4553638fad7c
Create Date: 2022-05-11 11:19:03.622637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8872236155f1'
down_revision = '4553638fad7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pitch_category'), 'pitch', ['category'], unique=False)
    op.create_index(op.f('ix_pitch_title'), 'pitch', ['title'], unique=False)
    op.create_index(op.f('ix_pitch_username'), 'pitch', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pitch_username'), table_name='pitch')
    op.drop_index(op.f('ix_pitch_title'), table_name='pitch')
    op.drop_index(op.f('ix_pitch_category'), table_name='pitch')
    op.drop_table('pitch')
    # ### end Alembic commands ###