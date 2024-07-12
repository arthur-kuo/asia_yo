# _*_ coding: UTF-8 _*_

import sys
import os
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)


import unittest
from unittest.mock import patch
from fastapi import HTTPException
from app.dependencies.processor import OrderProcessor


class TestOrderProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = OrderProcessor()

    def test_name_contains_non_english_characters(self):
        order = {'name': 'JohnDoe測試'}
        with self.assertRaises(HTTPException) as cm:
            self.processor.process_order(order)
        self.assertEqual(cm.exception.status_code, 400)
        self.assertEqual(
            cm.exception.detail,
            "Name contains non-English characters"
        )

    def test_name_not_capitalized(self):
        order = {'name': 'john doe'}
        with self.assertRaises(HTTPException) as cm:
            self.processor.process_order(order)
        self.assertEqual(cm.exception.status_code, 400)
        self.assertEqual(cm.exception.detail, "Name is not capitalized")

    def test_price_over_2000(self):
        order = {'name': 'John Doe', 'price': '2500'}
        with self.assertRaises(HTTPException) as cm:
            self.processor.process_order(order)
        self.assertEqual(cm.exception.status_code, 400)
        self.assertEqual(cm.exception.detail, "Price is over 2000")

    def test_currency_format_wrong(self):
        order = {'name': 'John Doe', 'price': '1500', 'currency': 'JPY'}
        with self.assertRaises(HTTPException) as cm:
            self.processor.process_order(order)
        self.assertEqual(cm.exception.status_code, 400)
        self.assertEqual(cm.exception.detail, "Currency format is wrong")

    @patch(
        'app.dependencies.processor.CurrencyConverter.convert',
        return_value=15500.0
    )
    def test_convert_usd_to_twd(self, mock_convert):
        order = {'name': 'John Doe', 'price': '500', 'currency': 'USD'}
        processed_order = self.processor.process_order(order)
        self.assertEqual(processed_order['price'], '15500.0')
        self.assertEqual(processed_order['currency'], 'TWD')


if __name__ == '__main__':
    unittest.main()
