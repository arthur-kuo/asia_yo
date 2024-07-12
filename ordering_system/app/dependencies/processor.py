# _*_ coding: UTF-8 _*_

from .validators import NameValidator, PriceValidator
from .currency import CurrencyConverter


class OrderProcessor:
    def __init__(self):
        self.name_validator = NameValidator()
        self.price_validator = PriceValidator()

    def process_order(self, order: dict) -> dict:
        self.name_validator.validate(order['name'])
        self.price_validator.validate(order['price'])

        if order['currency'] != "TWD":
            currency_converter = CurrencyConverter(order['currency'])
            order['price'] = str(
                currency_converter.convert(float(order['price']))
            )
            order['currency'] = "TWD"  # 將所有貨幣轉換成台幣

        return order
