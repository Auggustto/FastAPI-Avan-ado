'''
    VAMOS FAZER 2 EXEMPLOS 
    UM SYNCRONO E OUTRO ASYNCRONO
    USANDO A PREPARAÇÃO DE UMA LANCHE
'''
from time import sleep
import asyncio

#  FORMA SYNCRONA
class SyncCook:
    
    def cook_brad(self):
        sleep(3)

    def cook_hamburger(self):
        sleep(10)

    def mouth_sandwich(self):
        sleep(3)

    def make_milkshake(self):
        sleep(5)
        
    def cook(self):
        self.cook_brad()
        self.cook_hamburger()
        self.mouth_sandwich()
        self.make_milkshake()
        
# sync_cook = SyncCook()
# sync_cook.cook() # time cook: real 0m21,019s


# FORMA ASYNCRONA
class AsyncCook:
    
    async def cook_brad(self):
        await asyncio.sleep(3)

    async def cook_hamburger(self):
        await asyncio.sleep(10)

    async def mouth_sandwich(self):
        await asyncio.sleep(3)

    async def make_milkshake(self):
        await asyncio.sleep(5)
        
    async def cook(self):
        
        await asyncio.gather(
            self.cook_brad(),
            self.cook_hamburger(),
            self.make_milkshake()
        )
        
        await self.mouth_sandwich()
        
# async_cook = AsyncCook()
# asyncio.run(async_cook.cook()) # time cook: real  0m13,087s


# DEIXANDO O CÓDIGO MAIS RÁPIDO
class NewAsyncCook:
    
    async def cook_brad(self):
        await asyncio.sleep(3)

    async def cook_hamburger(self):
        await asyncio.sleep(10)

    async def mouth_sandwich(self):
        await asyncio.sleep(3)

    async def make_milkshake(self):
        await asyncio.sleep(5)
        
    '''
        Pegando a finalizaçao da tarefa para iniciar outra 
        assim melhorando o tempo
    '''
    async def make_sandwich(self):
        await asyncio.gather(
            self.cook_brad(),
            self.cook_hamburger(),
        )
        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.mouth_sandwich())
        
        
        
    async def cook(self):
        
        await asyncio.gather(
            self.make_milkshake(),
            self.make_sandwich()
        )
        
async_cook = NewAsyncCook()
asyncio.run(async_cook.cook()) # time cook: real 0m10,080s