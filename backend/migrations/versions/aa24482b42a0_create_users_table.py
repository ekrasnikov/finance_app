"""create users table

Revision ID: aa24482b42a0
Revises: 
Create Date: 2023-02-23 23:55:57.605965

"""
from datetime import datetime
from uuid import uuid4

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa24482b42a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.UUID, primary_key=True, default=uuid4()),
        sa.Column('login', sa.String(100), nullable=False, unique=True),
        sa.Column('hashed_password', sa.String(100), nullable=False),
        sa.Column('created_at', sa.DateTime(), default=datetime.now())
    )


def downgrade():
    op.drop_table('users')
