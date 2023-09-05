import io
import sys
from setuptools import setup

def get_cmdclass():
  """Build an abi3 (forward compatible) wheel when `setup.py bdist_wheel` is called."""
  if sys.version_info[0] == 2:
    return {}

  try:
    from wheel.bdist_wheel import bdist_wheel
  except ImportError:
    return {}

  class bdist_wheel_abi3(bdist_wheel):
    def get_tag(self):
      python, abi, plat = bdist_wheel.get_tag(self)
      return python, "abi3", plat

  return {"bdist_wheel": bdist_wheel_abi3}

def read(path, mode="rt", encoding="utf-8"):
    with io.open(path, mode=mode, encoding=encoding) as fp:
        return fp.read()

setup(
  name="python-libmagic",
  packages=["magic"],
  url="https://github.com/dveselov/python-libmagic",
  author="Dmitry Veselov",
  author_email="d.a.veselov@yandex.ru",
  version="0.5.0",
  description="Python bindings to libmagic",
  long_description=read("README.md"),
  long_description_content_type="text/markdown",
  license="MIT",
  classifiers=[
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
  ],
  # cffi>=1.8 for Py_LIMITED_API forward compatibility ref https://cffi.readthedocs.io/en/latest/cdef.html
  install_requires=["cffi>=1.8"],
  setup_requires=["cffi>=1.8"],
  python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*",
  cffi_modules=["magic/magic_build.py:ffibuilder"],
  cmdclass=get_cmdclass(),
  extras_require={"test": ["pytest", 'pre-commit~=3.4 ; python_version >= "3.6"']}
)
