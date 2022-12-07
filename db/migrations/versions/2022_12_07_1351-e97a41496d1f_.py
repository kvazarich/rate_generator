"""empty message

Revision ID: e97a41496d1f
Revises: 
Create Date: 2022-12-07 13:51:27.837448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e97a41496d1f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tickervalue',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('ticker_id', sa.BigInteger(), nullable=True),
    sa.Column('value', sa.BigInteger(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ticker_id'], ['ticker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tickervalue_time'), 'tickervalue', ['time'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tickervalue_time'), table_name='tickervalue')
    op.drop_table('tickervalue')
    # ### end Alembic commands ###