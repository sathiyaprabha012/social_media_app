"""create votes table

Revision ID: b9a0eda231de
Revises: f6d078e02c28
Create Date: 2025-06-02 19:55:08.244834

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9a0eda231de'
down_revision: Union[str, None] = 'f6d078e02c28'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# user_id = Column( Integer , ForeignKey ("users.id" , ondelete = "CASCADE") , primary_key = True)
#     post_id = Column( Integer , ForeignKey ("posts.id" , ondelete = "CASCADE") , primary_key = True)
def upgrade() -> None:
    op.create_table("votes" ,
                    sa.Column("user_id" , sa.Integer() , sa.ForeignKey ("users.id" , ondelete = "CASCADE") , primary_key = True) ,
                    sa.Column("post_id" , sa.Integer() , sa.ForeignKey ("posts.id" , ondelete = "CASCADE") , primary_key = True) 
    )


def downgrade() -> None:
    op.drop_table("votes")
