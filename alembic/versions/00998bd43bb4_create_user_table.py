"""create user table

Revision ID: 00998bd43bb4
Revises: 
Create Date: 2024-11-01 17:17:38.786586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00998bd43bb4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tbl_user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), unique=True, nullable=False),
        sa.Column('password_hash', sa.String(128), nullable=False),
        sa.Column('email', sa.String(120), unique=True, nullable=False),
        sa.Column('is_active', sa.Boolean, default=True, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'), 
                 onupdate=sa.text('CURRENT_TIMESTAMP'), nullable=False)
    )



def downgrade() -> None:
    op.drop_table("tbl_user")
