"""insert initial roles

Revision ID: e685fb1b511e
Revises: 743c4223aa05
Create Date: 2026-02-11 13:26:14.271660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e685fb1b511e'
down_revision: Union[str, Sequence[str], None] = '743c4223aa05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    op.bulk_insert(
        sa.table(
            "roles",
            sa.column("name", sa.String),
            sa.column("description", sa.String),
            sa.column("created_ad", sa.String),
        ),
        [
            {
                "name": "ADMIN",
                "description": "Administrador del sistema",
                "created_ad": "system",
            },
            {
                "name": "USER",
                "description": "Usuario estándar",
                "created_ad": "system",
            },
            {
                "name": "MANAGER",
                "description": "Gestor del sistema",
                "created_ad": "system",
            },
        ],
    )


def downgrade():
    op.execute(
        """
        DELETE FROM roles
        WHERE name IN ('ADMIN', 'USER', 'MANAGER')
        """
    )