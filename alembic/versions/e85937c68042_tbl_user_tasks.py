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
    pass


def downgrade() -> None:
    pass
