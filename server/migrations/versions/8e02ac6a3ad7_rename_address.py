"""rename address

Revision ID: 8e02ac6a3ad7
Revises: 8165a03748f1
Create Date: 2025-03-26 12:44:18.813618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e02ac6a3ad7'
down_revision = '8165a03748f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address', new_column_name='location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location', new_column_name='address')


    # ### end Alembic commands ###
