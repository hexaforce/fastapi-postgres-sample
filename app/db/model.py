# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Company(Base):
    __tablename__ = 'companies'
    __table_args__ = {'comment': '企業テーブル'}

    id = Column(UUID, primary_key=True, server_default=text("gen_random_uuid()"), comment='企業ID')
    sf_account_id = Column(String, comment='Salesforce企業ID')
    updated_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))
    created_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))


class Product(Base):
    __tablename__ = 'products'
    __table_args__ = (
        UniqueConstraint('company_id', 'product_name'),
        {'comment': '商材テーブル'}
    )

    id = Column(UUID, primary_key=True, server_default=text("gen_random_uuid()"), comment='商材ID')
    product_name = Column(String, comment='商材名')
    company_id = Column(ForeignKey('companies.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, comment='企業ID')
    updated_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))
    created_at = Column(DateTime(True), server_default=text("CURRENT_TIMESTAMP"))
    hearing_complete = Column(Boolean, server_default=text("false"), comment='ヒアリング完了フラグ')

    company = relationship('Company')
