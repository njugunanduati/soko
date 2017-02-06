"""empty message

Revision ID: ae7b580f3e46
Revises: None
Create Date: 2017-02-01 12:35:36.860307

"""

# revision identifiers, used by Alembic.
revision = 'ae7b580f3e46'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_reset', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_reset')
    ### end Alembic commands ###