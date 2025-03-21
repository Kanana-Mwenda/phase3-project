"""add columns to owners table

Revision ID: 699968362912
Revises: 9c40c545fee0
Create Date: 2025-03-12 15:35:24.941307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '699968362912'
down_revision: Union[str, None] = '9c40c545fee0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('owners', sa.Column('name', sa.String(), nullable=True))
    op.add_column('owners', sa.Column('email', sa.String(), nullable=True))
    op.add_column('owners', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('owners', 'phone_number')
    op.drop_column('owners', 'email')
    op.drop_column('owners', 'name')
    # ### end Alembic commands ###
