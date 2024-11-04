"""alter table user add columns

Revision ID: a3cf034192d2
Revises: e85937c68042
Create Date: 2024-11-04 14:25:22.168617

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3cf034192d2'
down_revision: Union[str, None] = 'e85937c68042'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
