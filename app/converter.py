from os import getenv
import requests
from fastapi import HTTPException
import aiohttp


ALPHAVANTAGE_APIKEY = getenv('ALPHAVANTAGE_APIKEY')

async def converter(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APIKEY}'
    
    try:
        #  Request async
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()
                print(data)
            
        if "Realtime Currency Exchange Rate" not in data:
            raise HTTPException(status_code=400, detail=f"Realtime Currency Exchange Rate not in response: {data}")
        
        exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        
        return {to_currency: price * exchange_rate}
        
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)