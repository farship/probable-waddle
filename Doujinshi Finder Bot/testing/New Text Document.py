from bs4 import BeautifulSoup as bs
import requests
import random
import time


def rng(sauce):
    numbers = str(random.randint(240000,318275))
    sauce = ("https://nhentai.net/g/" + numbers + "/")
    print ("RNG Link: " + sauce)
    soup_link = sauce
    make_soup(soup_link)

def make_soup(s_link):
    url = requests.get(s_link)
    soup = bs(url.content, 'html.parser')
    soup_html = str(soup)
    print ("Soup Link: " + s_link)
    tests_link = s_link
    tests(soup_html, tests_link)

def tests(html, t_link):
    if "404 - Not Found" in html:
        print ("Error: 404")
        raise Exception

    else:
        pass

    if "language/english" in html:
        print ("English Passed")
        print ("Tests-Lang Link: " + t_link)
    else:
        print ("Not English")
        raise Exception

    banned_tags = ["lolicon", "ugly-bastard", "yaoi", "guro"]
    for x in banned_tags:
        if x in html:
            print("Contians: " + x)
            raise Exception
    print("Safe: " + t_link)

    

def start_up():
    try:
        rng('')
    except Exception:
        time.sleep(0.25)
        start_up()

#start_up()
