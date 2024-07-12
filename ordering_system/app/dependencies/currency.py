# _*_ coding: UTF-8 _*_

from fastapi import HTTPException
from .exchange_rates import exchange_rates


class CurrencyConverter:
    def __init__(self, currency: str):
        self.currency = currency

    def convert(self, price: float) -> float:
        if self.currency not in exchange_rates:
            raise HTTPException(
                status_code=400,
                detail="Currency format is wrong"
            )
        rate = exchange_rates[self.currency]
        return price * rate
