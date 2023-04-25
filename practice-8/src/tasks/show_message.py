from celery import shared_task

@shared_task
def show_message(symbol: str) -> None:
  print(f'The price for {symbol} has been requested')