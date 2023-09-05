# https://cffi.readthedocs.io/en/latest/cdef.html?highlight=Py_LIMITED_API#out-of-line-api
import cffi

ffibuilder = cffi.FFI()
ffibuilder.set_source("magic._magic", "#include <magic.h>", libraries=["magic"])
ffibuilder.cdef("""
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

if __name__ == "__main__":
  ffibuilder.compile(verbose=True)
