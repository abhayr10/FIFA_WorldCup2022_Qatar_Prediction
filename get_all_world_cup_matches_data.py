#WEB SCRAPING
#Python and BeautifulSoup

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

years = [1930,1934,1938,1950,1954,1958,1962,1966,1970,1974,1978,1982,1986,1990,1994,1998,2002,2006,2010,2014,2018]


#Creating a function named 'get_all_wc_matches' to get the teams and score of matches played in the world cup
def get_all_wc_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    response = requests.get(web)        #requests to get info of the website
    content=response.text               #response.text helps in providing the info in text format
    soup = bs(content, 'lxml')

    #Finding all the matches into the list named 'match'
    matches = soup.find_all('div',class_='footballbox')               

    #Creating list for scores, home and away teams
    home_team=[]
    score=[]
    away_team=[]
    for match in matches:
        home_team.append(match.find('th',class_='fhome').get_text())
        score.append(match.find('th',class_='fscore').get_text())
        away_team.append(match.find('th',class_='faway').get_text())

    dict_football = {'home_team':home_team,'score':score,'away_team':away_team}

    football_df = pd.DataFrame(dict_football)
    football_df['year'] = year
    return football_df
    
# All World Cups' Data
fifa = [get_all_wc_matches(year) for year in years]
df_fifa = pd.concat(fifa,ignore_index=True)
df_fifa.to_csv('all_fifa_wc_resultsdata.csv',index=False)

# 2022 World Cups Fixtures
df_fixtures = get_all_wc_matches(2022)
df_fixtures.to_csv('2022fifa_wc_fixtures.csv', index=False)