from typing import List, cast
import psycopg2
from psycopg2 import sql

def persist(tickers: List[str]) -> None:
  with psycopg2.connect('dbname=ticker user=tsvetan') as connection:
    with connection.cursor() as cursor:
      stmt = sql.SQL("insert into Monitored values (%s)")

      cursor.execute(stmt, (tickers, ))

def get_all() -> List[str]:
  with psycopg2.connect('dbname=ticker user=tsvetan') as connection:
    with connection.cursor() as cursor:
      cursor.execute('SELECT * FROM Monitored')
      all_tickers = cursor.fetchone()
      if all_tickers == None:
        return []
      return cast(List, all_tickers)[0]