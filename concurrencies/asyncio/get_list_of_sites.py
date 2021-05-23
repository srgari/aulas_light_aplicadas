# collected from https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp

import aiohttp
import asyncio 
import time 
import os 
import re

curdir = os.path.dirname(__file__)
os.chdir(curdir)

async def __get_list_of_sites():

    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.sinapsebiotecnologia-loja.com.br') as response:

            print('Status:', response.status)
            print('Content type:', response.headers['content-type'])

            global html
            html = await response.text()
            print('body:', html[:15], '...')
            title = re.findall('<title>(.*)</title>', html)[0]
            
        

def generate_list_of_sites():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(__get_list_of_sites())    
    l = re.findall('href="(.*)?/"', html)
    return l

if __name__ == '__main__':
    l = generate_list_of_sites()

# ###########################################
# ### agora o bicho pega 
# ##########################################
# s = time.time()


# async def get_site(session, url):
#     async with session.get(url) as resp:
#         html = await resp.text()        
#         title = re.findall('<title>(.*)</title>', html)
#         if len(title) > 0:
#             with open(title[0].replace('/','_')+'.html', 'w') as x:
#                 x.write(html)

# async def main():

#     async with aiohttp.ClientSession() as session:
        
#         tasks = []
#         for url in l:
#             print(f'\nconnecting to {url}\n')
#             tasks.append(asyncio.ensure_future(get_site(session, url)))
        
#         original_site = await asyncio.gather(*tasks)
        

# asyncio.run(main())
# e = time.time()
# print(f'ftime: {(e-s):.2f}')