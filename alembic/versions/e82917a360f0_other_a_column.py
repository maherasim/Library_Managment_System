"""other  a column

Revision ID: e82917a360f0
Revises: 3ace4235ab26
Create Date: 2023-04-04 19:55:38.622325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e82917a360f0'
down_revision = '3ace4235ab26'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('book', sa.Column('copies', sa.String(21)))

def downgrade():
    op.drop_column('book', 'copies')