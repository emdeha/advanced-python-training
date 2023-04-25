import mongoengine as me

class TickerList(me.Document):
  tickers = me.ListField() # type: ignore[attr-defined]