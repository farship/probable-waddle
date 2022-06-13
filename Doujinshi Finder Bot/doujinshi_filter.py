import Doujinshi_Finder_Bot as DFB

from bs4 import BeautifulSoup as bs
import requests
import random
import time

def rng(sauce): #rng_tag
    numbers = str(random.randint(240000,318275))
    sauce = ("https://nhentai.net/g/" + numbers + "/")
    #print ("RNG Link: " + sauce)
    soup_link = sauce
    make_soup(soup_link) #rng_tag

def make_soup(s_link): #soup_tag
    url = requests.get(s_link, stream=True)
    soup = bs(url.content, 'html.parser')
    soup_html = str(soup)
    #print ("Soup Link: " + s_link)
    tests_link = s_link
    tests(soup_html, tests_link) #soup_tag

def tests(html, t_link): #test_tag
    if "404 - Not Found" in html:
        print ("Error: 404")
        raise Exception

    else:
        pass

    if "language/english" in html:
        #print ("English Passed")
        #print ("Tests-Lang Link: " + t_link)
        pass
    else:
        print ("Not English")
        raise Exception
    banned_tags = ["rape","lolicon", "shotacon", "hairy", "pregnant", "urination", "yaoi", "scat", "inflation", "bestiality", "monster", "old-man", "enema", "oppai-loli", "guro", "urine", "prolapse", "vore", "vomit"]
    for x in banned_tags:
        if x in html:
            print("Contains: " + x)
            raise Exception
    #print("Safe: " + t_link)
    if len(DFB.tags) == 0:
        print ("No tags selected")
        pass
    else:
        for x in DFB.tags:
            if x in html:
                print ('Has: ' + x)
                pass
            else:
                print ('No: ' + x)
                raise Exception
    print ("DONE")
    global random_link
    random_link = t_link


def find_random():
    global tries
    try:
        if tries >= 30:
            raise SyntaxWarning
        print (str(tries))
        rng('')
    except SyntaxWarning:
        print ("Sorry, but I couldn't find that after " + str(tries) + " tries.")
    except Exception:
        time.sleep(0.05)
        tries += 1
        find_random()

def find_wholesome():
    rndNum = str(random.randint(1,1700))
    url = 'https://wholesomelist.com/list#{}'.format(rndNum)
    req = requests.get(url)
    soup = (bs(req.content, 'html.parser'))
    soupsplit1 = str(soup).split('<td>{}'.format(rndNum))[1]
    splitonA = soupsplit1.split('href="')[1]
    global splitafter
    splitafter = splitonA.split('"')[0]
