from setuptools import setup

setup(**{
  "name": "python-libmagic",
  "packages": ["magic"],
  "url": "https://github.com/dveselov/python-libmagic",
  "author": "Dmitry Veselov",
  "author_email": "d.a.veselov@yandex.ru",
  "version": "0.4.0",
  "description": "Python bindings to libmagic",
  "license": "MIT",
  "classifiers": (
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
  ),
  "install_requires": [
    "cffi==1.7.0",
  ],
})
