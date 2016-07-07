from . import ffi
from . import flags

__version__ = "0.4.0"


class Magic(object):

  def __init__(self, initial_flags=flags.MAGIC_MIME_TYPE, database=None):
    cookie = ffi.open(initial_flags)
    if database:
      ffi.load(cookie, database)
    else:
      ffi.load(cookie)
    self.cookie = cookie

  def __del__(self):
    try:
      ffi.close(self.cookie)
    except Exception as exception:
      raise
  
  def __enter__(self):
    return self
  
  def __exit__(self, type, value, traceback):
    del self

  @property
  def version(self):
    return ffi.version()

  def set_flags(self, flags):
    return ffi.set_flags(self.cookie, flags)

  def handle_bytes(function):
    def wrapper(self, value):
      if not isinstance(value, bytes):
        value = value.encode("utf-8")
      response = function(self, value)
      return response.decode("utf-8")
    return wrapper

  @handle_bytes
  def from_file(self, filepath):
    return ffi.file(self.cookie, filepath)

  @handle_bytes
  def from_buffer(self, value):
    return ffi.buffer(self.cookie, value)
