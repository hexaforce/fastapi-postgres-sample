"""empty message

Revision ID: 4224450f13be
Revises: 
Create Date: 2022-12-21 02:40:35.841187

"""
import sqlalchemy as sa
from alembic import op
from db.alembic_ext import ReplaceableObject
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4224450f13be'
down_revision = None
branch_labels = None
depends_on = None


update_timestamp = ReplaceableObject(
    "update_timestamp()",
    """
   RETURNS trigger
   LANGUAGE 'plpgsql'
   COST 100
   VOLATILE NOT LEAKPROOF
   AS $BODY$
   BEGIN
     NEW.updated_at = current_timestamp;
     RETURN NEW;
   END; $BODY$;
   """,
)


updated_at_companies = ReplaceableObject(
    "updated_at_companies",
    """
    BEFORE UPDATE 
    ON companies
    FOR EACH ROW
    EXECUTE PROCEDURE update_timestamp();
    """,
)

drop_trigger_companies = ReplaceableObject(
    "updated_at_companies ON companies",
    """
    """,
)

updated_at_products = ReplaceableObject(
    "updated_at_products",
    """
    BEFORE UPDATE 
    ON products
    FOR EACH ROW
    EXECUTE PROCEDURE update_timestamp();
    """,
)

drop_trigger_products = ReplaceableObject(
    "updated_at_products ON products",
    """
    """,
)

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute('CREATE EXTENSION IF NOT EXISTS "pgcrypto"')
    op.create_function(update_timestamp)

    op.create_table('companies',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('gen_random_uuid()'), autoincrement=False, nullable=False, comment='企業ID'),
    sa.Column('sf_account_id', sa.VARCHAR(), autoincrement=False, nullable=True, comment='Salesforce企業ID'),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='companies_pkey'),
    comment='企業テーブル',
    postgresql_ignore_search_path=False
    )

    op.create_table('products',
    sa.Column('id', postgresql.UUID(), server_default=sa.text('gen_random_uuid()'), autoincrement=False, nullable=False, comment='商材ID'),
    sa.Column('product_name', sa.VARCHAR(), autoincrement=False, nullable=True, comment='商材名'),
    sa.Column('company_id', postgresql.UUID(), autoincrement=False, nullable=False, comment='企業ID'),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('hearing_complete', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=True, comment='ヒアリング完了フラグ'),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name='products_company_id_fkey', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='products_pkey'),
    sa.UniqueConstraint('company_id', 'product_name', name='products_company_id_product_name_key'),
    comment='商材テーブル',
    postgresql_ignore_search_path=False
    )

    op.create_trigger(updated_at_companies)

    op.create_trigger(updated_at_products)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_trigger(drop_trigger_products)

    op.drop_trigger(drop_trigger_companies)

    op.drop_table('products')

    op.drop_table('companies')
    # ### end Alembic commands ###
