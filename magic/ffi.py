from cffi import FFI
from . import flags


ffi = FFI()
ffi.cdef("""
  typedef ... magic_set;
  typedef struct magic_set *magic_t;
  magic_t magic_open(int);
  void magic_close(magic_t);
  const char *magic_getpath(const char *, int);
  const char *magic_file(magic_t, const char *);
  const char *magic_descriptor(magic_t, int);
  const char *magic_buffer(magic_t, const void *, size_t);
  const char *magic_error(magic_t);
  int magic_setflags(magic_t, int);
  int magic_version(void);
  int magic_load(magic_t, const char *);
  int magic_compile(magic_t, const char *);
  int magic_check(magic_t, const char *);
  int magic_list(magic_t, const char *);
  int magic_errno(magic_t);
""")

magic = ffi.verify("""
  #include <magic.h>
""", libraries=["magic"])

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

def open(flags=flags.MAGIC_NONE):
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

def file(cookie, path):
  mimetype = magic.magic_file(cookie, path)
  if mimetype == ffi.NULL:
    message = error(cookie)
    raise ValueError(message)
  else:
    return ffi.string(mimetype)

def buffer(cookie, value):
  mimetype = magic.magic_buffer(cookie, value, len(value))
  if mimetype == ffi.NULL:
    message = error(cookie)
    raise ValueError(message)
  else:
    return ffi.string(mimetype)
