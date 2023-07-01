from aiohttp import ClientSession
from fastapi import FastAPI

app = FastAPI()

@app.get("/ticker/{symbol}")
async def ticker(symbol):
  async with ClientSession() as session:
    async with session.get(
        f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules=financialData',
      ) as response:

      content = await response.json()

      quote = content['quoteSummary']['result'][0]['financialData']
      open = quote['currentPrice']['fmt']
      financialCurrency = quote['financialCurrency']

      return f'Price for {symbol} - {open} {financialCurrency}'
