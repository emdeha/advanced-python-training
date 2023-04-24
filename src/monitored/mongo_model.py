import mongoengine as me

class Monitored(me.Document):
  tickers = me.ListField() # type: ignore[attr-defined]