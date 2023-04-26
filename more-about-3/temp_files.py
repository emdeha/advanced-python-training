import tempfile

class TempFile:
  def __init__(self):
    self.tempfile = tempfile.TemporaryFile()

  def __enter__(self):
    return self.tempfile

  def __exit__(self, exception_type, exception_val, trace):
    self.tempfile.close()

with TempFile() as tmp:
  tmp.write(b'test')
  tmp.seek(0)
  print(tmp.read(4))