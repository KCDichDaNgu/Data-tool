"""empty message

Revision ID: 0f4d314361a2
Revises: 33a7f303b61a
Create Date: 2020-12-01 22:33:21.606512

"""

# revision identifiers, used by Alembic.
revision = '0f4d314361a2'
down_revision = '33a7f303b61a'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'screen_size',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)
    op.drop_column('product', 'resolution')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('resolution', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.alter_column('product', 'screen_size',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###
