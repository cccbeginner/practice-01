"""create user table

Revision ID: 015b95890a72
Revises: 
Create Date: 2023-05-21 20:18:41.233342

"""
from alembic import op
from sqlalchemy import Column, Date, DateTime, String
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '015b95890a72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        Column('username', String, primary_key=True),
        Column('password', String, nullable=False),
        Column('birthday', Date),
        Column('create_time', DateTime, default=func.now()),
        Column('last_login', DateTime, nullable=True)
    )


def downgrade():
    pass
