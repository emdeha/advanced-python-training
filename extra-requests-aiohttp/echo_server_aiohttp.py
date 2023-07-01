from aiohttp import web
import requests

async def ticker(request: web.Request) -> web.Response:
  symbol = request.match_info['symbol']
  response = requests.get(
    f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules=financialData',
    headers={
      'User-Agent': '',
    },
  )
  content = response.json()

  quote = content['quoteSummary']['result'][0]['financialData']
  open = quote['currentPrice']['fmt']
  financialCurrency = quote['financialCurrency']

  return web.Response(text=f'Price for {symbol} - {open} {financialCurrency}')

if __name__ == "__main__":
  app = web.Application()
  app.add_routes([web.post('/ticker/{symbol}', ticker)])
  web.run_app(app, host='localhost', port=1337)
