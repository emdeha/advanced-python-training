from flask import Flask

from echo.flask_view import EchoAPI
from ticker.flask_view import TickerAPI

from .config import Config

def serve() -> None:
  app = Flask(__name__)

  app.config.from_object(Config())

  app.add_url_rule('/', view_func=EchoAPI.as_view('echo-api'), endpoint='/')
  app.add_url_rule('/ticker/<symbol>', view_func=TickerAPI.as_view('ticker-api'), endpoint='/ticker/<symbol>')
 
  app.run(debug=True, use_reloader=True)