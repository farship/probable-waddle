from bs4 import BeautifulSoup as bs
import requests
import time
def daily_astronomy(write_this):
    url = 'https://apod.nasa.gov/apod/astropix.html'
    req = requests.get(url)
    soup = bs(req.content, 'html.parser')
    d2 = str(soup)
    s1 = 'src="image'
    i1 = d2.split(s1,1)[1]
    s2 = '"'
    i2 = i1.split(s2,1)[0]
    #image/\
    #text \/
    s3 = '<center>\n<b>'
    i3 = d2.split(s3,1)[1]
    s4 = '<p> <center>'
    i4 = i3.split(s4,1)[0]
    
    #f = open("daily_astronomy.html", "w")
    write_this = ('<head> <meta http-equiv="refresh" content="3600"> \n<link rel="icon" href="https://apod.nasa.gov/favicon.ico"></head> \n<title>Daily Astronomy</title> \n<img src=https://apod.nasa.gov/apod/image' + i2 +'>\n<centre>\n<b><br/>' + i4)
    global thisone
    thisone = write_this
    print ('Done1')
    #time.sleep(1)
    #f.write('<head> <meta http-equiv="refresh" content="3600"> \n<link rel="icon" href="https://apod.nasa.gov/favicon.ico"></head> \n<title>Daily Astronomy</title> \n<img src=https://apod.nasa.gov/apod/image' + i2 +'>\n<centre>\n<b><br/>' + i4)
    #f.close()
    #time.sleep(10)#7200
    #daily_astronomy(write_this)
def apod_loop():
    try:
        daily_astronomy('')
    except Exception:
        print ('NO IMAGE')
        #time.sleep(10)#7200
        pass
