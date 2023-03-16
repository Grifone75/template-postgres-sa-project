"""create base table

Revision ID: fb7ddddd772c
Revises: 
Create Date: 2023-03-16 15:26:36.400716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb7ddddd772c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'base',
        sa.Column('id',sa.Integer, primary_key=True),
        sa.Column('name',sa.String(50), nullable=False),
        sa.Column('description',sa.Unicode(200)),
    )


def downgrade() -> None:
    op.drop_table('base')
