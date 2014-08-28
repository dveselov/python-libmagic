from . import ffi
from . import flags

__version__ = "0.2.0"


class Magic(object):

  def __init__(self, database=None, debug=False, mimetype=False, encoding=False,
                     compress=False, follow_symlinks=False):
    initial = flags.MAGIC_NONE
    if debug:
      initial |= flags.MAGIC_DEBUG
    if mimetype:
      if encoding:
        initial |= flags.MAGIC_MIME
      else:
        initial |= flags.MAGIC_MIME_TYPE
    if compress:
      initial |= flags.MAGIC_COMPRESS
    if follow_symlinks:
      initial |= flags.MAGIC_SYMLINK
    cookie = ffi.open(initial)
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
  
  def __exit__(self):
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
