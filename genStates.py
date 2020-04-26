import requests
import lxml
from bs4 import BeautifulSoup
import os

URL = 'https://geographic.org/streetview/usa/'
print(URL)
page = requests.get(URL)
bigDaddy = []
soup = BeautifulSoup(page.content, 'lxml')

states = soup.find('ul')
for x in range(len(states.find_all('a'))):
    content = states.find_all('a')[x]
    currentState = content.get('href').split("/")[0]
    os.mkdir(currentState)
    f = open(currentState + '/genCounties.py', 'w')
    f.write("""

import requests
import lxml
import numpy
from bs4 import BeautifulSoup
import sys
import os

STATE = os.getcwd().split("\\\\")[-1]
URL = 'https://geographic.org/streetview/usa/' + STATE.lower() + '/'
print(URL)
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')

for i in range(len(soup.find_all('li'))):
    currentCounty = soup('li')[i].text
    os.mkdir(currentCounty)
    f = open(currentCounty + '/genCities.py', 'w')
    f.write(\"\"\"

import requests
import lxml
import numpy
from bs4 import BeautifulSoup
import sys
import os

STATE = os.getcwd().split("\\\\\\\\")[-2]
COUNTY = os.getcwd().split("\\\\\\\\")[-1]
URL = 'https://geographic.org/streetview/usa/' + STATE.lower() + '/' + COUNTY.lower().replace(" ", "_") + '/'
print(URL)
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')

for i in range(len(soup.find_all('li'))):
    currentCity = soup('li')[i].text
    os.mkdir(currentCity)
    f = open(currentCity + '/genStreets.py', 'w')
    f.write(\\"\\"\\"
import requests
import lxml
from bs4 import BeautifulSoup
import json
import os

STATE = os.getcwd().split("\\\\\\\\\\\\\\\\")[-3]
COUNTY = os.getcwd().split("\\\\\\\\\\\\\\\\")[-2]
CITY = os.getcwd().split("\\\\\\\\\\\\\\\\")[-1]

URL = 'https://geographic.org/streetview/usa/' + STATE.lower() + '/' + COUNTY.lower() + '/' + CITY.lower() + '.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')

def getStreets():
    URL = 'https://geographic.org/streetview/usa/' + STATE.lower() + '/' + COUNTY.lower().replace(" ", "_") + '/' + CITY.lower().replace(" ", "_") + '.html'
    print(URL)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'lxml')
    streets = []
    for x in range(len(soup.find_all('li'))):
        street = ['','']
        txt = soup('li')[x].text
        street[0] = txt.split(" \\\\\\\\xa0 ")[0]
        street[1] = txt.split(" \\\\\\\\xa0 ")[1]
        streets.append(street)
        continue
    return streets


streets = getStreets()
output = json.dumps(streets)
f = open('streets.json', 'w')
f.write(json.dumps(streets))
f.close()

for x in range(len(streets)):
    street = streets[x-1]
    print("Zip = ", street[1], ", Street = ", street[0])
    \\"\\"\\")
    \"\"\")
    f.close()
    """)
    f.close()