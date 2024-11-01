"""tbl user membership

Revision ID: 30cdf19e39a7
Revises: 57e872c34c2a
Create Date: 2024-11-01 17:43:58.144201

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30cdf19e39a7'
down_revision: Union[str, None] = '57e872c34c2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 创建用户会员关联表
    op.create_table(
        'tbl_user_membership',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('membership_level_id', sa.Integer, nullable=False),
        sa.Column('start_date', sa.DateTime, nullable=False, comment='会员开始时间'),
        sa.Column('end_date', sa.DateTime, nullable=False, comment='会员结束时间'),
        sa.Column('created_at', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'), 
                 onupdate=sa.text('CURRENT_TIMESTAMP'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('tbl_user_membership')