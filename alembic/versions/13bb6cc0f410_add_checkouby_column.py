"""Add checkouby column

Revision ID: 13bb6cc0f410
Revises: 50fc642bb911
Create Date: 2023-04-06 23:38:44.536743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13bb6cc0f410'
down_revision = '50fc642bb911'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Books', 
                  
                  sa.Column('checked_out_by1', sa.String(20),nullable=True)
                  
                  
                  )

def downgrade():
    op.drop_column('Books', 'checked_out_by1')