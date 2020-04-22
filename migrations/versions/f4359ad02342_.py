"""empty message

Revision ID: f4359ad02342
Revises: 03210d9ecbd0
Create Date: 2020-04-21 22:11:02.494493

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f4359ad02342'
down_revision = '03210d9ecbd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Actor', 'birthday')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Actor', sa.Column('birthday', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###