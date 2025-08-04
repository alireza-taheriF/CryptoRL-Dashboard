from fastapi import APIRouter, HTTPException
from services.coingecko import get_live_prices

router = APIRouter(prefix="/price")

@router.get("/live")
def get_live_price():
    try:
        prices = get_live_prices()
        return prices
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))