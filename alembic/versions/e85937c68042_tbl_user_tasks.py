"""tbl user tasks

Revision ID: e85937c68042
Revises: 30cdf19e39a7
Create Date: 2024-11-01 17:50:12.520030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM

# 创建任务状态枚举类型
task_status = ENUM('in_progress', 'completed', 'cancelled', name='task_status')

# revision identifiers, used by Alembic.
revision: str = 'e85937c68042'
down_revision: Union[str, None] = '30cdf19e39a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tbl_user_tasks',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('task_name', sa.String(100), nullable=False, comment='任务名称'),
        sa.Column('task_description', sa.String(500), nullable=True, comment='任务描述'),
        sa.Column('created_time', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'), comment='创建时间'),
        sa.Column('updated_time', sa.DateTime, server_default=sa.text('CURRENT_TIMESTAMP'), 
                 onupdate=sa.text('CURRENT_TIMESTAMP'), comment='更新时间'),
        sa.Column('progress', sa.Float, default=0.0, comment='任务进度(0-100)'),
        sa.Column('status', sa.String(20), default='pending', comment='任务状态(pending/running/completed/failed)'),
    )


def downgrade() -> None:
    op.drop_table('tbl_user_tasks')
