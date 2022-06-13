from bs4 import BeautifulSoup as bs
import requests
import time
from flask import Flask,redirect
import gkeepapi as gka
import datetime

global keep
keep = gka.Keep()

global spm
spm = '"'
global qum
qum = "'"
global buttons
buttons = '<button onclick="location.href=' + qum + "/" + qum + ';">APOD and Forecast</button>' + '<button onclick="location.href=' + qum + "/apod" + qum + ';">APOD</button>' + '<button onclick="location.href=' + qum + "/forecast" + qum + ';">Forecast</button>' + '<button onclick="location.href=' + qum + "/pi" + qum + ';">Pi Version</button>' + '<button onclick="location.href=' + qum + "/gallery" + qum + ';">Gallery</button>' + '<button onclick="location.href=' + qum + "/list" + qum + ';">List</button>'

def pi_daily_astronomy():
    global thisone
    url = 'https://apod.nasa.gov/apod/astropix.html'
    req = requests.get(url)
    soup = bs(req.content, 'html.parser')
    d2 = str(soup)
    try:
        i1 = d2.split('src="image',1)[1]
        i2 = i1.split('"',1)[0]
    except:
        i1 = ""
        i2 = '/2001/RubinsGalaxy_hst2000.jpg'
    i3 = d2.split('<center>\n<b>',1)[1]
    i4 = i3.split('<p> <center>',1)[0]
    keep.login('peterhendry10@gmail.com', 'nttmlyibtjbmmgdq')
    gnote = keep.get('1WL_Hf5SId8F7Xj0A2Cy4hRgDN3xgiBHxce10sHKwYsklh94uD7En-0u41ao0Q_RVXDUM')
    notes_title = gnote.title
    notes_text = gnote.text.replace('\n','<br>')
    forecast = '</div><div id = column_middle><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g7_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C"><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g7.ASP?LOCATIONID=59641&CO=UK&U=C"><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g24_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C"><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g24.ASP?LOCATIONID=59641&CO=UK&U=C"></div></div>'
    dt = datetime.datetime.now()
    currentDate = dt.strftime("%A %d %B %Y")
    notes = '<div id = column_right> <h1>' + currentDate + '</h1> <h>' + notes_title + '</h><p>' + notes_text + '</p></div></body>'
    columns = '<head><style>body {background-color: rgb(8,8,8); color: white;} #column_left {float: left; width: 40%;} #column_middle {float: left; width: 28%; margin-left: 10px;} #column_right { float: left; width: 30%; margin-left: 10px;} img {max-width: 100%;max-height: 25%;}</style><meta http-equiv="refresh" content="3600"><link rel="icon"href="https://apod.nasa.gov/favicon.ico">' + buttons + '</head><title>Daily Astronomy</title><head><meta name="viewport"content="width=device-width, initial-scale=1"></head><body><div><div id= column_left>'
    write_this = (columns + '<br><img src=' + spm + 'https://apod.nasa.gov/apod/image' + i2 + spm + '>\n<centre>\n<b><br/>' + i4 + forecast + notes)
    thisone = write_this
    return thisone

def daily_astronomy():
    global thisone
    url = 'https://apod.nasa.gov/apod/astropix.html'
    req = requests.get(url)
    soup = bs(req.content, 'html.parser')
    d2 = str(soup)
    try:
        i1 = d2.split('src="image',1)[1]
        i2 = i1.split('"',1)[0]
    except:
        i1 = ""
        i2 = '/2001/RubinsGalaxy_hst2000.jpg'
    i3 = d2.split('<center>\n<b>',1)[1]
    i4 = i3.split('<p> <center>',1)[0]
    
    forecast = '</div><div id = column_middle><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g7_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C"><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g7.ASP?LOCATIONID=59641&CO=UK&U=C"><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g24_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C"><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g24.ASP?LOCATIONID=59641&CO=UK&U=C"></div></div>'
    dt = datetime.datetime.now()
    currentDate = dt.strftime("%A %d %B %Y")
    notes = '<div id = column_right> <h1>' + currentDate + '</h1></div></body>'
    columns = '<head><style>body {background-color: rgb(8,8,8); color: white;} #column_left {float: left; width: 40%;} #column_middle {float: left; width: 28%; margin-left: 10px;} #column_right { float: left; width: 30%; margin-left: 10px;} img {max-width: 100%;max-height: 25%;}</style><meta http-equiv="refresh" content="3600"><link rel="icon"href="https://apod.nasa.gov/favicon.ico">' + buttons + '</head><title>Daily Astronomy</title><head><meta name="viewport"content="width=device-width, initial-scale=1"></head><body><div><div id= column_left>'
    write_this = (columns + '<br><img src=' + spm + 'https://apod.nasa.gov/apod/image' + i2 + spm + '>\n<centre>\n<b><br/>' + i4 + forecast + notes)
    thisone = write_this
    return thisone

def getToDo():
    global thisone
    url = 'https://apod.nasa.gov/apod/astropix.html'
    req = requests.get(url)
    soup = bs(req.content, 'html.parser')
    d2 = str(soup)
    try:
        i1 = d2.split('src="image',1)[1]
        i2 = i1.split('"',1)[0]
    except:
        i1 = ""
        i2 = '/2001/RubinsGalaxy_hst2000.jpg'
    i3 = d2.split('<center>\n<b>',1)[1]
    i4 = i3.split('<p> <center>',1)[0]
    keep.login('peterhendry10@gmail.com', 'nttmlyibtjbmmgdq')
    gnote = keep.get('1GKg4-xNfVlrD1JiGArbIpf5LD0wAOX6-TFogCrz2dQAFPmQBOKZWreaNbZD4Tg')
    notes_title = gnote.title
    notes_text = gnote.text.replace('\n','<br>')
    forecast = '</div><div id = column_middle><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g7_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C"><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g7.ASP?LOCATIONID=59641&CO=UK&U=C"><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g24_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C"><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g24.ASP?LOCATIONID=59641&CO=UK&U=C"></div></div>'
    dt = datetime.datetime.now()
    currentDate = dt.strftime("%A %d %B %Y")
    notes = '<div id = column_right> <h1>' + currentDate + '</h1> <h>' + notes_title + '</h><p>' + notes_text + '</p></div></body>'
    columns = '<head><style>body {background-color: rgb(8,8,8); color: white;} #column_left {float: left; width: 40%;} #column_middle {float: left; width: 28%; margin-left: 10px;} #column_right { float: left; width: 30%; margin-left: 10px;} img {max-width: 100%;max-height: 25%;}</style><meta http-equiv="refresh" content="3600"><link rel="icon"href="https://apod.nasa.gov/favicon.ico">' + buttons + '</head><title>Daily Astronomy</title><head><meta name="viewport"content="width=device-width, initial-scale=1"></head><body><div><div id= column_left>'
    write_this = (columns + '<br><img src=' + spm + 'https://apod.nasa.gov/apod/image' + i2 + spm + '>\n<centre>\n<b><br/>' + i4 + forecast + notes)
    thisone = write_this
    return thisone


def getApod():
    global backupImage
    global thisone
    url = 'https://apod.nasa.gov/apod/astropix.html'
    req = requests.get(url)
    soup = bs(req.content, 'html.parser')
    d2 = str(soup)
    try:
        i1 = d2.split('src="image',1)[1]
        i2 = i1.split('"',1)[0]
    except:
        i1 = ""
        i2 = '/2001/RubinsGalaxy_hst2000.jpg'
    i3 = d2.split('<center>\n<b>',1)[1]
    i4 = i3.split('<p> <center>',1)[0]
    return '<head><style>body {background-color: rgb(8,8,8); color: white;}</style><meta http-equiv="refresh" content="3600"><link rel="icon"href="https://apod.nasa.gov/favicon.ico">' + buttons + '</head><title>Daily Astronomy</title><br><img src="https://apod.nasa.gov/apod/image' + i2 + '"\n<centre>\n<b><br/>' + i4

def getForecast():
    return '<head><style>body {background-color: rgb(8,8,8); color: white;}</style><meta http-equiv="refresh" content="900, http://192.168.0.114:5000/pi"><link rel="icon"href="https://apod.nasa.gov/favicon.ico">' + buttons + '</head><title>Daily Astronomy</title><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g7_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C"width=50%><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g7.ASP?LOCATIONID=59641&CO=UK&U=C"width=50%><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g24_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C"width = 50%><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g24.ASP?LOCATIONID=59641&CO=UK&U=C"width=50%>'

app = Flask(__name__)
@app.route('/')
def apod_forecast():
    try:
        return daily_astronomy()
    except:
        print ('APOD FORECAST LOOP')
        return redirect('http://192.168.0.44:5000/forecast', code = 302)

@app.route('/pi')
def pi_apod_forecast():
    try:
        return pi_daily_astronomy()
    except:
        print('PI APOD FORECAST LOOP')
        return redirect("http://192.168.0.44:5000/forecast")

@app.route('/apod')
def onlyApod():
    try:
        return getApod()
    except:
        print ('GET APOD EXCEPTION')
        return redirect("http://192.168.0.44:5000/forecast")

@app.route('/forecast')
def onlyForecast():
    try:
        return getForecast()
    except:
        print ('GET FORECAST EXCEPTION')
        return redirect("http://192.168.0.44:5000/forecast")

@app.route('/gallery')
def galleryRoute():
    try:
        return open('/home/pi/astroPortfolio.html','r').read()
    except:
        print ('GALLERY EXCEPTION')
        return redirect("http://192.168.0.44:5000/forecast")
@app.route('/list')
def toDoList():
    try:
        return getToDo()
    except:
        print ('LIST EXCEPTION')
        return redirect("http://192.168.0.44:5000/forecast")

if __name__ == '__main__': # netstat
    app.run(host='0.0.0.0', debug=True, port=5000) #192.168.0.19 is PC      192.168.0.44 / 'raspberrypi' is RP

