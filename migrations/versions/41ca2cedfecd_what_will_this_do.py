"""what will this do?

Revision ID: 41ca2cedfecd
Revises: 
Create Date: 2019-09-19 08:41:30.063334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41ca2cedfecd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('props', sa.JSON(), nullable=True),
    sa.Column('registeredon', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_device_name'), 'device', ['name'], unique=False)
    op.create_index(op.f('ix_device_userid'), 'device', ['userid'], unique=False)
    op.create_table('game_object',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('game', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=256), nullable=True),
    sa.Column('pw_hash', sa.String(length=128), nullable=True),
    sa.Column('createdon', sa.Date(), nullable=True),
    sa.Column('lastlogin', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('user_location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('long', sa.Numeric(), nullable=True),
    sa.Column('lat', sa.Numeric(), nullable=True),
    sa.Column('elev', sa.Numeric(), nullable=True),
    sa.Column('timestamp', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_location')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('game_object')
    op.drop_index(op.f('ix_device_userid'), table_name='device')
    op.drop_index(op.f('ix_device_name'), table_name='device')
    op.drop_table('device')
    # ### end Alembic commands ###
