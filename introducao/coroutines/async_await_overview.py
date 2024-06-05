import asyncio

#  função syncrona
def sync_sum(a,b):
    
    return a + b


async def async_sum(a,b):
    
    return a + b

soma = async_sum(5,5)


#  EVENT LOOP
# 1° EXEMPLO

event_loop = asyncio.new_event_loop()
result = event_loop.run_until_complete(soma)
print(result)