"""new fields in user model

Revision ID: 975c5ed1371f
Revises: 48e8f659eadf
Create Date: 2021-08-05 09:01:18.845290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '975c5ed1371f'
down_revision = '48e8f659eadf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
