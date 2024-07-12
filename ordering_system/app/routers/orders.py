# _*_ coding: UTF-8 _*_

from fastapi import APIRouter, HTTPException
from ..dependencies.input_model import OrderModel
from ..dependencies.processor import OrderProcessor

router = APIRouter()
order_processor = OrderProcessor()


@router.post("/orders")
def orders(order: OrderModel):
    try:
        processed_order = order_processor.process_order(
            order.dict()
        )
        return processed_order
    except HTTPException as e:
        raise e
