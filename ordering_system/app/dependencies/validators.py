# _*_ coding: UTF-8 _*_

from abc import ABC, abstractmethod
from fastapi import HTTPException


class IValidator(ABC):
    @abstractmethod
    def validate(self, subject: str) -> None:
        pass


class NameValidator(IValidator):
    def validate(self, name: str) -> None:
        if not name.isascii():
            raise HTTPException(
                status_code=400,
                detail="Name contains non-English characters"
            )
        if not all(word[0].isupper() for word in name.split()):
            raise HTTPException(
                status_code=400,
                detail="Name is not capitalized"
            )


class PriceValidator(IValidator):
    def validate(self, price: str) -> None:
        if float(price) > 2000:
            raise HTTPException(
                status_code=400,
                detail="Price is over 2000"
            )
