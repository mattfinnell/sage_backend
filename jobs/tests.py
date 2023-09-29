from django.test import TestCase
import urllib3
from .barcode.barcode_handler import BarcodeHandler
from pprint import pprint


class BarcodeHandlerTestCase(TestCase):
    def setUp(self):
        self._fixture = BarcodeHandler(urllib3.PoolManager())
        self._url = (
            "https://mattfinnell-sage-test-data.s3.amazonaws.com/mamalils-label.jpg"
        )

    def test_happy_path(self):
        expected, actual = (
            # "Crispy Green Non-GMO Crispy Fruit - 4 Pack All Mango ",
            "Mama Lil’s",
            self._fixture.handle(self._url),
        )

        # pprint(actual)
        self.assertEqual(actual['product']['product_name_en'], expected)
