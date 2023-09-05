from ._magic import ffi, lib as magic


def handle_null_exception(function):
  def wrapper(cookie, *args, **kwargs):
    response = function(cookie, *args, **kwargs)
    if response == ffi.NULL:
      message = error(cookie)
      raise ValueError(message)
    else:
      return ffi.string(response)
  return wrapper

def version():
  return magic.magic_version()

def set_flags(cookie, flags):
  status = magic.magic_setflags(cookie, flags)
  if status != 0:
    message = error(cookie)
    raise ValueError(message)
  else:
    return True

def error(cookie):
  message = magic.magic_error(cookie)
  return ffi.string(message)

def open(flags):
  cookie = magic.magic_open(flags)
  if cookie == ffi.NULL:
    message = error(cookie)
    raise RuntimeError(message)
  else:
    return cookie

def close(cookie):
  closed = magic.magic_close(cookie)
  return True

def load(cookie, path=ffi.NULL):
  status = magic.magic_load(cookie, path)
  if status != 0:
    message = error(cookie)
    raise ValueError(message)
  else:
    return True

@handle_null_exception
def file(cookie, path):
  mimetype = magic.magic_file(cookie, path)
  return mimetype

@handle_null_exception
def buffer(cookie, value):
  mimetype = magic.magic_buffer(cookie, value, len(value))
  return mimetype
