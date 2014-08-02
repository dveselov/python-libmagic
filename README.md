# python-libmagic

![magic.h](http://i.imgur.com/GbN8szC.jpg)

# Usage

```python
import magic
import magic.flags

magic = magic.Magic(mimetype=True)

mimetype = magic.from_buffer("\x89\x50\x4E\x47\x0D\x0A\x1A\x0A")
print mimetype # => "image/png"

mimetype = magic.from_filepath("/etc/passwd")
print mimetype # => "text/plain"

updated = magic.set_flags(magic.flags.MAGIC_NONE)
print updated # => True
mimetype = magic.from_filepath("demo.docx")
print mimetype # => "Microsoft Word 2007+"
```

# Installation

```bash
$ apt-get install libmagic-dev
$ pip install python-libmagic
```

# License

Licensed under MIT license.
