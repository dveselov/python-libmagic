from distutils.core import setup

setup(**{
  'name': 'python-libmagic',
  'packages': ['magic'],
  'url': 'https://github.com/tyrannosaurus/python-libmagic',
  'author': 'python-libmagic contributors',
  'author_email': 'github@require.pm',
  'version': '0.1.0',
  'description': 'Python bindings to libmagic',
  'license': 'MIT',
  'classifiers': (
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
  ),
  'install_requires': [
    'cffi==0.8',
  ],
})
