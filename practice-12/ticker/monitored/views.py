from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_api_key import permissions
from .serializers import MonitoredSerializer

import urllib
import json

from .models import Monitored

class MonitoredViewSet(viewsets.ModelViewSet):
  queryset = Monitored.objects.all()
  serializer_class = MonitoredSerializer
  permission_classes = [permissions.HasAPIKey]

  def _show_stats(self, ticker: str) -> tuple[str, str]:
    response = urllib.request.urlopen(f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=financialData')
    content = json.loads(response.read().decode('utf-8'))

    quote = content['quoteSummary']['result'][0]['financialData']
    open = quote['currentPrice']['fmt']
    financialCurrency = quote['financialCurrency']

    return (open, financialCurrency)

  def list(self, request: Request, pk=None) -> Response:
    tickers = Monitored.objects.all()[0].tickers
    result = []
    for ticker in tickers:
      stats = self._show_stats(ticker)
      result.append(f'{ticker} - {stats[0]} {stats[1]}')
    return Response({'tickers': result})
