# python-libmagic

![magic.h](http://i.imgur.com/GbN8szC.jpg)

# Usage

```python
import magic

with magic.Magic() as m:
    print m.from_buffer("hello") # => "text/plain"
```

```python
import magic
import magic.flags

magic = magic.Magic()
mimetype = magic.from_buffer("\x89\x50\x4E\x47\x0D\x0A\x1A\x0A")
print mimetype # => "image/png"

mimetype = magic.from_file("/etc/passwd")
print mimetype # => "text/plain"

updated = magic.set_flags(magic.flags.MAGIC_NONE)
print updated # => True
mimetype = magic.from_file("demo.docx")
print mimetype # => "Microsoft Word 2007+"
magic.close() # don't forget about this
```

# Installation

`python-libmagic` works on CPython 2.7/3.3+ and PyPy.

```bash
$ apt-get install libmagic-dev
$ pip install python-libmagic
```

# License

Licensed under MIT license.
