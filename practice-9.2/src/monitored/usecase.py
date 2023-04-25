from typing import List

from monitored.monitored_model import Monitored
from ticker.usecase import showStats

def saveTickerList(tickers: List[str]) -> None:
  list = Monitored(tickers=tickers)
  list.save()

def getStats() -> List[str]:
  tickers = Monitored.objects[0].tickers
  result = []
  for ticker in tickers:
    stats = showStats(ticker)
    result.append(f'{ticker} - {stats[0]} {stats[1]}')
  return result