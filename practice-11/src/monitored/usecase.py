from typing import List
from sqlalchemy.engine import Engine

from monitored.sqlalchemy_repository import get_all, persist
from ticker.usecase import show_stats

def save_ticker_list(db: Engine, tickers: List[str]) -> None:
  persist(db, tickers)

def get_stats(db: Engine) -> List[str]:
  tickers = get_all(db)
  result = []
  for ticker in tickers:
    stats = show_stats(ticker)
    result.append(f'{ticker} - {stats[0]} {stats[1]}')
  return result