# _*_ coding: UTF-8 _*_

from pydantic import BaseModel


class AddressModel(BaseModel):
    city: str
    district: str
    street: str


class OrderModel(BaseModel):
    id: str
    name: str
    address: AddressModel
    price: str
    currency: str
