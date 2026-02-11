"""update role fields and seed manager

Revision ID: 024c42e38b41
Revises: e685fb1b511e
Create Date: 2026-02-11 14:09:08.271672

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '024c42e38b41'
down_revision: Union[str, Sequence[str], None] = 'e685fb1b511e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():

    # 🔥 1️⃣ Agregar nueva columna segura
    op.add_column(
        "roles",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("NOW()"),
            nullable=False
        )
    )

    # 🔥 2️⃣ Eliminar columna vieja (sin intentar convertirla)
    op.drop_column("roles", "created_ad")

    # 🔥 3️⃣ Agregar created_by
    op.add_column(
        "roles",
        sa.Column("created_by", sa.Integer(), nullable=True)
    )

    op.create_foreign_key(
        "fk_roles_created_by",
        "roles",
        "users",
        ["created_by"],
        ["id"]
    )

    # 🔥 4️⃣ Seed seguro MANAGER
    op.execute("""
    DO $$
    DECLARE
        v_user_id INT;
        v_role_id INT;
    BEGIN

        INSERT INTO users (email, password, is_active)
        VALUES (
            'manager@system.com',
            '$argon2id$v=19$m=65536,t=3,p=4$izHGmFOKsba2NmasFeJ8Dw$YboeyAC7l4k0EjrOG2Bh955nem6IB9D1pYsbfH2oBGs',
            TRUE
        )
        ON CONFLICT (email) DO NOTHING;

        SELECT id INTO v_user_id
        FROM users
        WHERE email = 'manager@system.com';

        INSERT INTO roles (name, description, created_by)
        VALUES (
            'MANAGER',
            'Manager del sistema',
            v_user_id
        )
        ON CONFLICT (name) DO NOTHING;

        SELECT id INTO v_role_id
        FROM roles
        WHERE name = 'MANAGER';

        INSERT INTO user_roles (user_id, role_id)
        VALUES (v_user_id, v_role_id)
        ON CONFLICT DO NOTHING;

    END $$;
    """)


def downgrade():

    op.execute("""
        DELETE FROM user_roles
        WHERE user_id IN (
            SELECT id FROM users WHERE email = 'manager@system.com'
        )
    """)

    op.execute("DELETE FROM roles WHERE name = 'MANAGER'")
    op.execute("DELETE FROM users WHERE email = 'manager@system.com'")

    op.drop_constraint("fk_roles_created_by", "roles", type_="foreignkey")
    op.drop_column("roles", "created_by")
    op.drop_column("roles", "created_at")
