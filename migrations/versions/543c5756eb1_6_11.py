"""6/11

Revision ID: 543c5756eb1
Revises: 456a945560f6
Create Date: 2016-06-11 17:52:42.819082

"""

# revision identifiers, used by Alembic.
revision = '543c5756eb1'
down_revision = '456a945560f6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    op.add_column('users', sa.Column('avatar_dir', sa.String(length=128), nullable=True))
    op.drop_column('users', 'role_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), nullable=True))
    op.drop_column('users', 'avatar_dir')
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###