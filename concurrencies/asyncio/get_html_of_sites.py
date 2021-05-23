###########################################
### agora o bicho pega 
### pegar todos os htmls de todas as páginas e juntar em um só
##########################################
from get_list_of_sites import *
import numpy as np

async def get_site(session, url):
    async with session.get(url) as resp:
        html = await resp.text()        
        title = re.findall('<title>(.*)</title>', html)

        if len(title) > 0:
            print(f'saving html {title}')
            with open(title[0].replace('/','_')+'.html', 'w') as x:
                x.write(html)
        lala.append('\n\n\n\n#########################' + html + '\n\n\n\n###############################')         


async def main():

    async with aiohttp.ClientSession() as session:
        
        tasks = []
        for url in l:
            print(f'\nconnecting to {url}\n')
            tasks.append(asyncio.ensure_future(get_site(session, url)))
        
        original_site = await asyncio.gather(*tasks)
        

def get_all_htmls():
    global lala
    lala = []
    s = time.time()
    global l
    l = generate_list_of_sites()
    asyncio.run(main())
    e = time.time()
    print(f'ftime: {(e-s):.2f}')
    return lala

if __name__ == '__main__':
    x = get_all_htmls()
    