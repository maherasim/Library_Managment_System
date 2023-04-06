"""Add a column

Revision ID: 19452abe812e
Revises: 20378615a92a
Create Date: 2023-04-03 09:38:55.736083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19452abe812e'
down_revision = '20378615a92a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('book', sa.Column('copies', sa.DateTime))

def downgrade():
    op.drop_column('book', 'copies')
