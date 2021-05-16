/home/user/Documents/git/aulas_light_aplicadas/airflow
import datetime
import os
import pathlib
import re
import time
from typing import List

from bs4 import BeautifulSoup
import pandas as pd
import requests


def fetch_day_agenda(date: str) -> List[str]:
    """
    Fetch appointments for the president for a specific date, 
    and returns a list of appointments

    Parameters:
    date (str) - string in a date format YYYY-MM-DD

    Example:
    fetch_day_agenda('2019-01-02')

    """
    url = f'https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica/{date}'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')

    list_of_appointments = []

    for start, end, title, place in zip(
            soup.find_all('time', 'compromisso-inicio'), 
            soup.find_all('time', 'compromisso-fim'), 
            soup.find_all('h4', 'compromisso-titulo'), 
            soup.find_all('div', 'compromisso-local')):

        list_of_appointments.append(dict(
            date=date,
            start_time=start.string, 
            end_time=end.string, 
            title=title.string, 
            place=place.string
            ))

    if len(list_of_appointments) == 0:
        list_of_appointments.append(dict(
            date=date,
            start_time='00h00',
            end_time='00h00',
            title='Nenhum compromisso',
            place='--'
            ))

    return list_of_appointments


def download_all_agenda(start_date:str = '2019-01-01',
        path_to_store_data:str ='./data'):
    """
    Download day agenda that are not already in a given folder.

    Parameters:
    start_date (str) - string in a date format YYYY-MM-DD to start scraping agenda
    path_to_store_data folder - string

    Example:
    download_all_agenda('2019-01-02')
    """
    pathlib.Path(path_to_store_data).mkdir(parents=True, exist_ok=True)
    dates = pd.Series(pd.date_range(start_date, datetime.date.today())).astype('str').tolist()
    downloaded_files = [re.sub('\.csv', '', file) for file in os.listdir(path_to_store_data)]
    dates_to_be_downloaded = [date for date in dates if date not in downloaded_files] 

    for date in dates_to_be_downloaded:
        try:
            df = pd.DataFrame(fetch_day_agenda(date))
            df.to_csv(os.path.join(path_to_store_data, f'{date}.csv'), index=False)
            time.sleep(1)
            print(f'data for day {date} saved.')
        except Exception as e:
            print(f'something went wrong when saving data for {date}: {e}')


def process_working_hours(path_to_data:str = './data', 
        path_to_store_data:str = './data/processed/'
        ): 

    files = os.listdir(path_to_data)
    df = pd.concat([pd.read_csv(os.path.join(path_to_data,file)) for file in files])

    df['duration'] = (pd.to_datetime(df['end_time'], format='%Hh%M') - pd.to_datetime(df['start_time'], format='%Hh%M'))
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df['duration'].resample('1D').sum()

    pathlib.Path(path_to_store_data).mkdir(parents=True, exist_ok=True)
    df.to_csv(path_to_store_data+'working_hours.csv')
    print('Wrote data processed dataframe')



def main():
    download_all_agenda('2021-05-10')
    process_working_hours()


if __name__ == '__main__':
    main()

