from typing import List

from monitored.psql_repository import persist, get_all
from ticker.usecase import show_stats

def save_ticker_list(tickers: List[str]) -> None:
  persist(tickers)

def get_stats() -> List[str]:
  tickers = get_all()
  result = []
  for ticker in tickers:
    stats = show_stats(ticker)
    result.append(f'{ticker} - {stats[0]} {stats[1]}')
  return result