"""create book table

Revision ID: 20378615a92a
Revises: 
Create Date: 2023-04-03 09:33:37.238812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20378615a92a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'book',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('author', sa.String(20)),
        sa.Column('pub_date', sa.Date()),
       
    )

def downgrade():
    op.drop_table('book')
