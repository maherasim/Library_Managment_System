"""Add a columnCHEK

Revision ID: 45bff4ed06c9
Revises: 4ba8054a8757
Create Date: 2023-04-08 21:46:40.894896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45bff4ed06c9'
down_revision = '4ba8054a8757'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('AUTHER', sa.String))

def downgrade():
    op.drop_column('account', 'AUTHER')
