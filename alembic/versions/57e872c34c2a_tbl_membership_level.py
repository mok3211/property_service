"""tbl membership level

Revision ID: 57e872c34c2a
Revises: 00998bd43bb4
Create Date: 2024-11-01 17:38:42.062923

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '57e872c34c2a'
down_revision: Union[str, None] = '00998bd43bb4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 创建会员等级表
    op.create_table(
        'tbl_membership_level',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, comment='会员等级名称'),
        sa.Column('price', sa.Numeric(10, 2), nullable=False, comment='会员价格'),
        sa.Column('duration_days', sa.Integer, nullable=False, comment='会员有效期(天)'),
        sa.Column('description', sa.String(200), comment='等级描述'),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'), 
                 onupdate=sa.text('CURRENT_TIMESTAMP'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('tbl_membership_level')
