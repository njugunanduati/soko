"""empty message

Revision ID: 5478d6543dec
Revises: 0ab352f9eb15
Create Date: 2017-01-25 12:45:59.124677

"""

# revision identifiers, used by Alembic.
revision = '5478d6543dec'
down_revision = '0ab352f9eb15'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product_sub_types', 'photo')
    op.drop_column('product_sub_types', 'description')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_sub_types', sa.Column('description', sa.VARCHAR(length=500), autoincrement=False, nullable=False))
    op.add_column('product_sub_types', sa.Column('photo', sa.VARCHAR(length=500), autoincrement=False, nullable=False))
    ### end Alembic commands ###