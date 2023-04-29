"""create Books table

Revision ID: 83ce74895e1a
Revises: 
Create Date: 2023-04-19 21:56:36.604609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83ce74895e1a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Books',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.String(200)),
        sa.Column('pub_by', sa.String(200)),
        sa.Column('copies', sa.String(200)),
        sa.Column('checked_out', sa.String(50), nullable=True),
        sa.Column('checked_out_by', sa.String(50), nullable=True),

    )

def downgrade():
    op.drop_table('account')