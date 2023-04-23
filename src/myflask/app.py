from flask import Flask

from echo.flask_view import echo_view
from ticker.flask_view import ticker_view

from .config import Config

def serve() -> None:
  app = Flask(__name__)

  app.config.from_object(Config())

  app.add_url_rule('/', view_func=echo_view, endpoint='/', methods=['POST'])
  app.add_url_rule('/ticker/<symbol>', view_func=ticker_view, endpoint='/ticker/<symbol>', methods=['POST'])
 
  app.run(debug=True, use_reloader=True)