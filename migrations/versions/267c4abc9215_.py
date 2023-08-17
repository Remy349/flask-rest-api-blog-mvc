"""empty message

Revision ID: 267c4abc9215
Revises: 959b638c49a0
Create Date: 2023-08-17 13:26:22.625036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '267c4abc9215'
down_revision = '959b638c49a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password_hash', sa.String(length=180), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###