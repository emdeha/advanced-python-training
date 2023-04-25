import json
import urllib.request

def run(symbol: str) -> tuple[str, str]:
  response = urllib.request.urlopen(f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules=financialData')
  content = json.loads(response.read().decode('utf-8'))

  quote = content['quoteSummary']['result'][0]['financialData']
  open = quote['currentPrice']['fmt']
  financialCurrency = quote['financialCurrency']

  return (open, financialCurrency)