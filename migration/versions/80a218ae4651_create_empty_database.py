"""Create empty database

Revision ID: 80a218ae4651
Revises: b82cfff2b6a5
Create Date: 2024-09-18 14:08:36.699627

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80a218ae4651'
down_revision: Union[str, None] = 'b82cfff2b6a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
