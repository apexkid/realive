"""empty message

Revision ID: 18552074ce1a
Revises: None
Create Date: 2015-04-25 17:38:17.506401

"""

# revision identifiers, used by Alembic.
revision = '18552074ce1a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('campaign',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('isactive', sa.Boolean(), nullable=False),
    sa.Column('isdeleted', sa.Boolean(), nullable=False),
    sa.Column('added_on', sa.DateTime(), nullable=False),
    sa.Column('modified_on', sa.DateTime(), nullable=False),
    sa.Column('city', sa.String(length=30), nullable=False),
    sa.Column('officeLocation', sa.String(length=100), nullable=False),
    sa.Column('localityPref', sa.String(length=100), nullable=False),
    sa.Column('poi', sa.String(length=100), nullable=False),
    sa.Column('livingCost', sa.Integer(), nullable=False),
    sa.Column('priorities', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('campaign')
    ### end Alembic commands ###
