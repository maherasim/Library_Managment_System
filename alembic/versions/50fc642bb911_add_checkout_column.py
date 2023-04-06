"""Add checkout column

Revision ID: 50fc642bb911
Revises: ccb88eb3a4ec
Create Date: 2023-04-06 22:46:59.191429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50fc642bb911'
down_revision = 'ccb88eb3a4ec'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Books', 
                  
                  sa.Column('checked_out_by', sa.String(20),nullable=False)
                  
                  
                  )

def downgrade():
    op.drop_column('Books', 'checked_out_by')