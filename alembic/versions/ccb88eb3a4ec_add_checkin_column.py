"""Add checkin column

Revision ID: ccb88eb3a4ec
Revises: 8a3edce51813
Create Date: 2023-04-06 22:39:44.273875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccb88eb3a4ec'
down_revision = '8a3edce51813'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('Books', 
                  
                  sa.Column('checked_out', sa.String)
                  
                  
                  )

def downgrade():
    op.drop_column('Books', 'checked_out')
