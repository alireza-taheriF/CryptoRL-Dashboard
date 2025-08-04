import requests
import time

_cached_data = None
_last_fetch_time = 0
CACHE_TTL = 30  # seconds

def get_live_prices():
    global _cached_data, _last_fetch_time

    now = time.time()
    if _cached_data and (now - _last_fetch_time) < CACHE_TTL:
        return _cached_data  # ⏪ داده کش‌شده

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,shiba-inu,tether",
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    _cached_data = response.json()
    _last_fetch_time = now
    return _cached_data
