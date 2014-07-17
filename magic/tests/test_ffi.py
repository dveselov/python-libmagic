import unittest
import magic.ffi
import magic.flags


class FFITestCase(unittest.TestCase):

  def test_version(self):
    version = magic.ffi.version()
    self.assertTrue(isinstance(version, int))

  def test_open(self):
    cookie = magic.ffi.open()
    self.assertNotEqual(cookie, None)

  def test_close(self):
    cookie = magic.ffi.open()
    self.assertNotEqual(cookie, None)
    closed = magic.ffi.close(cookie)
    self.assertTrue(closed)

  def test_load(self):
    cookie = magic.ffi.open()
    self.assertNotEqual(cookie, None)
    with self.assertRaises(ValueError):
      loaded = magic.ffi.load(cookie, b"/etc/magic_database")
    loaded = magic.ffi.load(cookie)
    self.assertTrue(loaded)

  def test_file(self):
    cookie = magic.ffi.open()
    self.assertNotEqual(cookie, None)
    loaded = magic.ffi.load(cookie)
    self.assertTrue(loaded)
    with self.assertRaises(ValueError):
      mimetype = magic.ffi.file(cookie, b"/etc/magic_database")
    mimetype = magic.ffi.file(cookie, b"/etc/passwd")
    self.assertEqual(mimetype, b"ASCII text")

  def test_buffer(self):
    cookie = magic.ffi.open()
    self.assertNotEqual(cookie, None)
    loaded = magic.ffi.load(cookie)
    self.assertTrue(loaded)
    mimetype = magic.ffi.buffer(cookie, b"")
    self.assertEqual(mimetype, b"empty")
    mimetype = magic.ffi.buffer(cookie, b"kittens")
    self.assertEqual(mimetype, b"ASCII text, with no line terminators")
    mimetype = magic.ffi.buffer(cookie, b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A")
    self.assertEqual(mimetype, b"PNG image data")

  def test_set_flags(self):
    cookie = magic.ffi.open()
    self.assertNotEqual(cookie, None)
    loaded = magic.ffi.load(cookie)
    self.assertTrue(loaded)
    mimetype = magic.ffi.buffer(cookie, b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A")
    self.assertEqual(mimetype, b"PNG image data")
    status = magic.ffi.set_flags(cookie, magic.flags.MAGIC_MIME_TYPE)
    self.assertTrue(status)
    mimetype = magic.ffi.buffer(cookie, b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A")
    self.assertEqual(mimetype, b"image/png")
    status = magic.ffi.set_flags(cookie, magic.flags.MAGIC_MIME)
    self.assertTrue(status)
    mimetype = magic.ffi.buffer(cookie, b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A")
    self.assertEqual(mimetype, b"image/png; charset=binary")
