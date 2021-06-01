"""update.user

Revision ID: 59070dc92ace
Revises: 778792fecc90
Create Date: 2021-06-01 11:03:23.754385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59070dc92ace'
down_revision = '778792fecc90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('github_userinfo', 'nickname',
                    existing_type=sa.VARCHAR(length=255),
                    nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('github_userinfo', 'email',
                    existing_type=sa.VARCHAR(length=255),
                    nullable=False)
    op.alter_column('github_userinfo', 'nickname',
                    existing_type=sa.VARCHAR(length=255),
                    nullable=False)
    # ### end Alembic commands ###