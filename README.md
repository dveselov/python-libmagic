# python-libmagic

CFFI bindings to libmagic1.

# Usage

```python
import magic

magic = magic.Magic(mime=True)
mimetype = magic.from_buffer("\x89\x50\x4E\x47\x0D\x0A\x1A\x0A")
print mimetype # => "image/png"
mimetype = magic.from_filepath("/etc/passwd")
print mimetype # => "ASCII text"
```

# License

Licensed under MIT license.
