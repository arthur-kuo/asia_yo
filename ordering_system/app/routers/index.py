# _*_ coding: UTF-8 _*_

from fastapi import APIRouter
from .orders import router as orders_router

router = APIRouter(prefix="/api")

router.include_router(orders_router)
