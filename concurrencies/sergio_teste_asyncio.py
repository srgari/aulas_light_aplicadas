#%%
import asyncio
# %%
async def count(): # this shit here is a COROUTINE, because it starts with async
    print('one')
    await asyncio.sleep(5) # using await or return creates a coroutine function
    print('two')

async def main():
    await asyncio.gather(count(), count(), count())

#%%
import time 
s2 = time.time()
asyncio.run(main())
#%%
elapsed = time.time() - s2
print(f'{__file__} executed in {elapsed:.2f} seconds')