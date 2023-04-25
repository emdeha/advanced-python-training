from flask import Flask
# To fix mypy "Missing library stubs" error, install the celery-stubs package
from celery import Celery, Task
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from echo.flask_view import EchoAPI
from ticker.ticker_view import TickerAPI
from monitored.view import MonitoredAPI

from monitored.sql_alchemy_model import Base

from .config import Config

def celery_init_app(app: Flask) -> Celery:
  class FlaskTask(Task):
    def __call__(self, *args: object, **kwargs: object) -> None:
      with app.app_context():
        return self.run(*args, **kwargs)

  celery_app = Celery(app.name, task_cls=FlaskTask)
  celery_app.config_from_object(app.config['CELERY'])
  celery_app.set_default()
  app.extensions['celery'] = celery_app
  return celery_app

def create_app() -> Flask:
  app = Flask(__name__)

  app.config.from_object(Config())
  app.config.from_prefixed_env()
  celery_init_app(app)

  return app

def setup_routing(app: Flask, db: Engine) -> None:
  app.add_url_rule('/', view_func=EchoAPI.as_view('echo-api'), endpoint='/')
  app.add_url_rule('/ticker/<symbol>', view_func=TickerAPI.as_view('ticker-api'), endpoint='/ticker/<symbol>')
  app.add_url_rule('/monitored', view_func=MonitoredAPI.as_view('monitored-api', db), endpoint='/monitored')

def create_db() -> Engine:
  engine = create_engine('postgresql://tsvetan@localhost/ticker')

  Base.metadata.create_all(engine)

  return engine

def serve() -> None:
  app = create_app()
  db = create_db()
  setup_routing(app, db)

  app.run(debug=True, use_reloader=True)