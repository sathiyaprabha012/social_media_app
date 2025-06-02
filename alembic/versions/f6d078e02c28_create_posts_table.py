"""create posts table

Revision ID: f6d078e02c28
Revises: 58b383896ae5
Create Date: 2025-06-02 19:45:01.195284

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6d078e02c28'
down_revision: Union[str, None] = '58b383896ae5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table ( "posts" ,
        sa.Column("id" , sa.Integer() , primary_key = True , nullable=False) ,
        sa.Column("title" , sa.String() , nullable = False ) ,
        sa.Column("content" , sa.String() , nullable = False) ,
        sa.Column("published" , sa.Boolean() , server_default = sa.text("TRUE") , nullable = True) ,
        sa.Column("created_at" , sa.TIMESTAMP(timezone = True ) , nullable = False , server_default = sa.text("now()")) ,
        sa.Column("owner_id" ,sa.Integer() , sa.ForeignKey("users.id" , ondelete = "CASCADE") , nullable = False)
    ) 



def downgrade() -> None:
    op.drop_table("posts")
