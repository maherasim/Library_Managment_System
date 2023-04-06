"""create user table

Revision ID: 3ace4235ab26
Revises: 19452abe812e
Create Date: 2023-04-03 09:40:27.436268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ace4235ab26'
down_revision = '19452abe812e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(20)),
        sa.Column('password', sa.String(100)),
       
    )

def downgrade():
    op.drop_table('book')
