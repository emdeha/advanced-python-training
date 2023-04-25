class Config(object):
  SERVER_NAME = 'localhost:1337'
  CELERY = dict(
    broker_url='redis://localhost',
    result_backend='redis://localhost',
    task_ignore_result=True,
  )
  MONGODB_SETTINGS = dict(
    db='myapp',
  )