
from bs4 import BeautifulSoup
from lxml import html
import requests
import pandas as pd

url= "http://www.ukforex.co.uk/exchange-rate"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)


table = soup.find("table", { "class" : "left" })
rows = table.find_all('tr')[1:]

data = {
    'mr' : [],
    'bid' : [],
    'ask' : [],

}
for row in rows:
    cols = row.find_all('td')
    data['mr'].append( cols[0].get_text() )
    data['bid'].append( cols[1].get_text() )
    data['ask'].append( cols[2].get_text() )

exData = pd.DataFrame( data )

print (data['mr'])