"""add google oauth fields to users

Revision ID: ab14df6335c8
Revises: 024c42e38b41
Create Date: 2026-02-18 17:12:50.207563
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab14df6335c8'
down_revision: Union[str, Sequence[str], None] = '024c42e38b41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1️⃣ Agregar columnas
    op.add_column(
        "users",
        sa.Column(
            "provider",
            sa.String(length=50),
            nullable=False,
            server_default="local"  # importante para usuarios existentes
        )
    )

    op.add_column(
        "users",
        sa.Column(
            "google_id",
            sa.String(length=255),
            nullable=True
        )
    )

    # 2️⃣ Crear constraint UNIQUE para google_id
    op.create_unique_constraint(
        "uq_users_google_id",
        "users",
        ["google_id"]
    )

    # 3️⃣ Quitar server_default (buena práctica)
    op.alter_column(
        "users",
        "provider",
        server_default=None
    )


def downgrade() -> None:
    # 1️⃣ Eliminar constraint
    op.drop_constraint(
        "uq_users_google_id",
        "users",
        type_="unique"
    )

    # 2️⃣ Eliminar columnas
    op.drop_column("users", "google_id")
    op.drop_column("users", "provider")