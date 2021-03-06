from unittest import TestCase
import gc


class BaseTmpl(TestCase):
    def setUp(self):
        print("{} start".format(self.id()))

    def tearDown(self):
        print("{} finish".format(self.id()))
        gc.collect()

    def assertEventNumber(self, data, expected_entries):
        entries = len([1 for entry in data["traceEvents"] if entry["ph"] != "M"])
        self.assertEqual(entries, expected_entries)
