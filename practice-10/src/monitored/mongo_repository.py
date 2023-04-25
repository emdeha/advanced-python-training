from typing import List

from monitored.mongo_model import Monitored

def persist(tickers: List[str]) -> None:
  list = Monitored(tickers=tickers)
  list.save()

def get_all() -> List[str]:
  return Monitored.objects[0].tickers # type: ignore