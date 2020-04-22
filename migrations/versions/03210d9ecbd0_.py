"""empty message

Revision ID: 03210d9ecbd0
Revises: 
Create Date: 2020-04-21 19:39:05.305479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03210d9ecbd0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Actor', sa.Column('birthday', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Actor', 'birthday')
    # ### end Alembic commands ###
