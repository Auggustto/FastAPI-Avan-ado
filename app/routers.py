from asyncio import gather
from fastapi import APIRouter, Path, Query
from app.converter import converter

from app.schamas import ConverterInput, ConverterOutPut

router = APIRouter(prefix='/converter')

@router.post("/{from_currency}", response_model=ConverterOutPut)
async def convert(
    #  Before Check Paramiters
    # from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$'),
    # to_currencies: str = Query(max_length=50, regex='^[A-Z]{3}(,[A-Z]{3})*$'),
    # price: float = Query(gt=0)
    
    #  New check paramitries
    body: ConverterInput,
    from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$')
    ):
    
    to_currencies = body.to_currencies
    price = body.price
        
    list_couroutines = []
    
    for currency in to_currencies:
        coro = converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        list_couroutines.append(coro)
    
    result = await gather(*list_couroutines)
    
    return ConverterOutPut(
        message="success",
        data=result
    )