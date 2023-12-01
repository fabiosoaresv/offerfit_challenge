"""create_event_table

Revision ID: 04b60511771b
Revises:
Create Date: 2023-12-01 15:19:59.095163

"""
from cgitb import text
import datetime
from typing import Sequence, Union

from alembic import op
from click import DateTime
import sqlalchemy as sa
print('passei aq')

# revision identifiers, used by Alembic.
revision: str = '04b60511771b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'events_test',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('customer_id', sa.Integer, nullable=False),
        sa.Column('event_type', sa.String, nullable=False),
        sa.Column('timestamp', DateTime, default=datetime.utcnow, server_default=text("(now() at time zone 'utc')"), nullable=False),
        sa.Column('email_id', sa.Integer, nullable=False),
        sa.Column('clicked_link', sa.String, nullable=True),
    )

def downgrade():
    op.drop_table('events')
