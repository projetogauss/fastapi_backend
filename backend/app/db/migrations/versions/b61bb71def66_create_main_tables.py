"""create_main_tables

Revision ID: b61bb71def66
Revises: 44d8c051c7c0
Create Date: 2021-04-08 00:33:26.618053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = 'b61bb71def66'
down_revision = '44d8c051c7c0'
branch_labels = None
depends_on = None

def create_cleanings_table() -> None:
    op.create_table(
        "cleanings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False, server_default="spot_clean"),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )

def upgrade() -> None:
    create_cleanings_table()

def downgrade() -> None:
    op.drop_table("cleanings")

