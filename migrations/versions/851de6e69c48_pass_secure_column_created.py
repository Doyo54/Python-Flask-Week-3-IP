"""pass_secure column created

Revision ID: 851de6e69c48
Revises: 22f8dbada732
Create Date: 2022-05-10 23:59:05.073761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '851de6e69c48'
down_revision = '22f8dbada732'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###