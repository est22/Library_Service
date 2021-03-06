"""empty message

Revision ID: 93e491923ff3
Revises: 
Create Date: 2021-08-28 01:10:49.047451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93e491923ff3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('author', sa.String(length=256), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=False),
    sa.Column('user_pw', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('book')
    # ### end Alembic commands ###
