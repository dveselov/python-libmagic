import unittest

import magic
import magic.flags


class MagicTestCase(unittest.TestCase):

  def setUp(self):
    self.magic = magic.Magic()

  def test_get_version(self):
    self.assertTrue(isinstance(self.magic.version, int))

  def test_from_buffer(self):
    mimetype = self.magic.from_buffer("ehlo")
    self.assertEqual(mimetype, "ASCII text, with no line terminators")

  def test_from_file(self):
    mimetype = self.magic.from_file("/etc/passwd")
    self.assertEqual(mimetype, "ASCII text")

  def test_set_flags(self):
    mimetype = self.magic.from_file("/etc/passwd")
    self.assertEqual(mimetype, "ASCII text")
    self.magic.set_flags(magic.flags.MAGIC_MIME_TYPE)
    mimetype = self.magic.from_file("/etc/passwd")
    self.assertEqual(mimetype, "text/plain")
