"""add enums

Revision ID: 5a077a981eb0
Revises: 3d7cb607c71d
Create Date: 2023-02-26 16:37:05.952802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a077a981eb0'
down_revision = '3d7cb607c71d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    actionsenm = sa.Enum('CREATE', 'READ', 'UPDATE', 'DELETE', name='actionsenm')
    actionsenm.create(op.get_bind())
    op.execute(
        'ALTER TABLE permission_actions ALTER COLUMN name TYPE actionsenm USING name::actionsenm'
    )

    targetsenum = sa.Enum('DOMAIN', 'USER', 'PERMISSION', 'TARGET', 'ROLE', name='targetsenum')
    targetsenum.create(op.get_bind())
    op.execute(
        'ALTER TABLE permission_targets ALTER COLUMN name TYPE targetsenum USING name::targetsenum'
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('permission_targets', 'name',
               existing_type=sa.Enum('DOMAIN', 'USER', 'PERMISSION', 'TARGET', 'ROLE', name='targetsenum'),
               type_=sa.VARCHAR(),
               existing_nullable=False)

    op.alter_column('permission_actions', 'name',
               existing_type=sa.Enum('CREATE', 'READ', 'UPDATE', 'DELETE', name='actionsenm'),
               type_=sa.VARCHAR(),
               existing_nullable=False)

    # Drop the actionsenm and targetsenum enum types
    actionsenm = sa.Enum('CREATE', 'READ', 'UPDATE', 'DELETE', name='actionsenm')
    actionsenm.drop(op.get_bind())
    targetsenum = sa.Enum('DOMAIN', 'USER', 'PERMISSION', 'TARGET', 'ROLE', name='targetsenum')
    targetsenum.drop(op.get_bind())
    # ### end Alembic commands ###