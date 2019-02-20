"""empty message

Revision ID: eab0fd8af7e6
Revises: 
Create Date: 2019-02-20 15:26:02.834378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eab0fd8af7e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('c_content', sa.String(), nullable=True),
    sa.Column('c_blog_id', sa.Integer(), nullable=True),
    sa.Column('c_com_posted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subscribe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('s_email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscribe_s_email'), 'subscribe', ['s_email'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=True),
    sa.Column('hash_pass', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('m_blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('m_blog_title', sa.String(), nullable=True),
    sa.Column('m_blog_content', sa.String(), nullable=True),
    sa.Column('m_blog_posted_on', sa.DateTime(), nullable=False),
    sa.Column('m_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['m_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('m_blog')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_subscribe_s_email'), table_name='subscribe')
    op.drop_table('subscribe')
    op.drop_table('comments')
    # ### end Alembic commands ###
