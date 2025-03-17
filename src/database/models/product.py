from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from sqlalchemy import Text, BigInteger, Boolean


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "product"
    article: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True)
    name: Mapped[str | None] = mapped_column(Text)
    price: Mapped[int] = mapped_column(BigInteger, default=0)
    rating: Mapped[int | None] = mapped_column(BigInteger)
    total_quantity: Mapped[int] = mapped_column(BigInteger, default=0)
    is_scheduled: Mapped[bool] = mapped_column(Boolean, default=False)
