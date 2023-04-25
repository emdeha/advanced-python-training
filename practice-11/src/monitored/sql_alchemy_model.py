from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import ARRAY, String

from typing import List

class Base(DeclarativeBase):
  pass

class Monitored(Base):
  __tablename__ = 'monitored'

  id: Mapped[int] = mapped_column(primary_key=True)
  tickers: Mapped[List[str]] = mapped_column(ARRAY(String))