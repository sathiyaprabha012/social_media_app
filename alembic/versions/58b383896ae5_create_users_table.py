"""create users table

Revision ID: 58b383896ae5
Revises: 
Create Date: 2025-06-02 19:21:49.358619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision: str = '58b383896ae5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None




def upgrade() -> None:
    op.create_table("users" , 
                    sa.Column("id",sa.Integer(),primary_key=True,nullable=False) , 
                    sa.Column("email",sa.String(),nullable=False,unique=True) , 
                    sa.Column("password",sa.String(),nullable=False) , 
                    sa.Column("created_at",sa.TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
                    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
