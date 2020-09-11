import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.skysports.com/premier-league-table/2019"
page = requests.get(url)
print(page)  # Response object

# obtain the html code behind the page
# print(page.text)

if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')
    # soup.prettify will return page.text contents in a structured format
    league = soup.find('table', class_ = 'standing-table__table')
    league_table = league.find_all('tbody')
    league_2020 = []

    for league_teams in league_table:
        rows = league_teams.find_all('tr')
        for row in rows:
            rank = row.find_all('td', class_ = 'standing-table__cell')[0].text.strip()
            team_name = row.find('td', class_ = 'standing-table__cell standing-table__cell--name').text.strip()
            PL = row.find_all('td', class_ = 'standing-table__cell')[2].text.strip()
            W = row.find_all('td', class_ = 'standing-table__cell')[3].text.strip()
            D = row.find_all('td', class_ = 'standing-table__cell')[4].text.strip()
            L = row.find_all('td', class_ = 'standing-table__cell')[5].text.strip()
            F = row.find_all('td', class_ = 'standing-table__cell')[6].text.strip()
            A = row.find_all('td', class_ = 'standing-table__cell')[7].text.strip()
            GD = row.find_all('td', class_ = 'standing-table__cell')[8].text.strip()
            team_points = row.find_all('td', class_ = 'standing-table__cell')[9].text.strip()

            league_dict = {
                '#': rank,
                'Name': team_name,
                'PL': PL,
                'W': W,
                'D': D,
                'L': L,
                'F': F,
                'A': A,
                'GD': GD,
                'Points': team_points}
            league_2020.append(league_dict)
    
    df = pd.DataFrame(league_2020)
    print(df)