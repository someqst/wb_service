from sqlalchemy.orm import mapped_column, DeclarativeBase
from sqlalchemy import Text, BigInteger


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'product'
    article = mapped_column(BigInteger, primary_key=True, unique=True)
    name = mapped_column(Text)
    price = mapped_column(BigInteger, default=0)
    rating = mapped_column(BigInteger)
    total_quantity = mapped_column(BigInteger, default=0)


class ScheduleProduct(Base):
    __tablename__ = 'schedule_product'
    article = mapped_column(BigInteger, primary_key=True, unique=True)
