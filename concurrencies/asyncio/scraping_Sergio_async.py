#%%
import pandas as pd
import asyncio
import httpx 
from random import choice
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore as F


async def get_html(dt: 'datetime64[ns]', cor: F) -> str:

    header = {'ACCEPT':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        
    print(cor + f'HTML do episódio do mês {dt.day}/{dt.month}/{dt.year}')

    baseURL = f'https://www.npr.org/series/423302056/hidden-brain/archive?date={str(dt)}'
    
    async with httpx.AsyncClient() as client:
        req = await client.get(baseURL, headers=header) # retorna uma taks
        req.raise_for_status()

        return req.text


def extract_info(text, cor, dt, d):
    soup = BeautifulSoup(text, features='lxml')
    for x in soup.find_all():
        if f'npr.org/{str(dt)[:4]}/' in str(x.get('href')) and len(x.get_text()) > 3 :
            link = x.get('href')
            text = x.get_text()
            if link not in list(d):
                d[link] = [text]    
            else:
                if text not in d[link]:
                    d[link].append(x.get_text())

    print(cor + f'HTML do episódio do mês {dt.day}/{dt.month}/{dt.year} -> FINALIZADO')
    return d


async def event():

    global d

    cores = [F.BLACK, F.RED, F.GREEN, F.YELLOW, F.BLUE, F.MAGENTA, F.CYAN, F.WHITE]

    tasks = []
    for data in datas:
        cor = choice(cores)
        tasks.append((data, loop.create_task(get_html(data, cor)), cor))

    for data, content, cor in tasks:
        html = await content
        d = extract_info(html, cor, data, d)


def main():
    global loop
    global d
    loop = asyncio.get_event_loop()
    loop.run_until_complete(event())

    return pd.DataFrame.from_dict(d, orient = 'index')

if __name__ == "__main__":
    d = {}
    datas = pd.date_range(start = '2011-01-01', end = pd.to_datetime('today'), freq = 'M')
    t0 = datetime.now()
    df = main()
    dt = datetime.now() - t0
    print(df.shape)
    print(f'Tempo total: {dt.total_seconds():.2f} segundos')
#%%