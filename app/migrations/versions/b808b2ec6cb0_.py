"""empty message

Revision ID: b808b2ec6cb0
Revises: 6a681f72f8e8
Create Date: 2022-12-09 00:21:01.904707

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b808b2ec6cb0'
down_revision = '6a681f72f8e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=16), nullable=True))
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=16),
               nullable=False)
        batch_op.alter_column('birthday',
               existing_type=sa.DATE(),
               nullable=False)
        batch_op.alter_column('birthplace',
               existing_type=mysql.VARCHAR(length=16),
               nullable=False)
        batch_op.drop_column('grade')

    with op.batch_alter_table('tournament', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=32),
               nullable=False)
        batch_op.alter_column('term',
               existing_type=mysql.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tournament', schema=None) as batch_op:
        batch_op.alter_column('term',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=32),
               nullable=True)

    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.add_column(sa.Column('grade', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.alter_column('birthplace',
               existing_type=mysql.VARCHAR(length=16),
               nullable=True)
        batch_op.alter_column('birthday',
               existing_type=sa.DATE(),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=mysql.VARCHAR(length=16),
               nullable=True)
        batch_op.drop_column('title')

    # ### end Alembic commands ###