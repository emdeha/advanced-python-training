from typing import List, cast

from sqlalchemy import select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from .sql_alchemy_model import Monitored

def persist(db: Engine, tickers: List[str]) -> None:
  with Session(db) as session:
    monitored = Monitored(tickers=tickers)
    session.add(monitored)
    session.commit()

def get_all(db: Engine) -> List[str]:
  with Session(db) as session:
    stmt = select(Monitored)
    monitored = session.scalar(stmt)
    if monitored == None:
      return []
    return cast(Monitored, monitored).tickers