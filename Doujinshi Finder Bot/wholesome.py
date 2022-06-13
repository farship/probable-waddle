from bs4 import BeautifulSoup as bs
import requests
import random
rndNum = str(random.randint(1,1700))
url = 'https://wholesomelist.com/list#{}'.format(rndNum)
req = requests.get(url)
soup = (bs(req.content, 'html.parser'))
soupsplit1 = str(soup).split('<td>{}'.format(rndNum))[1]
splitonA = soupsplit1.split('href="')[1]
splitafter = splitonA.split('"')[0]

