import youtube_dl
import datetime
#youtube-dl
#--geo-bypass
#--min-views int
#--max-views int
#--no playlist only video if playlist referenced
#--yes-playlist playlist if in the video url
#--playlist-reverse
#--newline prints progress on new lines
#--verbose logs lots of debugging info
#--format file format option
#   bestaudio or mp3
#   bestvideo or mp4
#--default-search str

#post-processing options
#--embed-thumbnail coverart from thumbnail
#--extract-audio
#--audio-quality 0



#URL

#-o '%(title)s.%(ext)s'

ydl_opts = {'geo-bypass' : False,
            'minviews' : 0,
            'maxviews' : 100000000000,
            'noplaylist' : True,
            'yesplaylist' : False,
            'playlist-reverse' : False,
            'newline' : True,
            'verbose' : True,
            'format' : 'bestaudio/best',
            'outmpl' : '/tempfiles/1.%(ext)s'#,
            #'defaultsearch' : ''
            }
def discord_default_music(url):
    ydl_opts = {'geo-bypass' : False,
            'minviews' : 0,
            'maxviews' : 100000000000,
            'noplaylist' : True,
            'yesplaylist' : False,
            'playlist-reverse' : False,
            'newline' : True,
            'verbose' : True,
            'format' : 'bestaudio',
            'outtmpl' : 'tempfiles/1.%(ext)s',#'/home/peter/Documents/Code/Doujinshi Finder Bot/tempfiles/1.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
            #'defaultsearch' : ''
            }
    youtube_dl.YoutubeDL(ydl_opts).download([url])
    return True


def download_with_options(url):
    url = input('URL: ')
    if url == 'n':
        url = input('Search: ')# append default search
    if input('Default Options? ') == 'y':
        defaultOptions = True
    else:
        defaultOptions = False
    for option in ydl_opts:
        if defaultOptions:
            break
        answer = input(option + ': ')
        if answer == 'y':
            option = True
        elif answer == 'n':
            option = False
        else:
            option = answer

    youtube_dl.YoutubeDL(ydl_opts).download([url])
#add options to variable, may need to be dictionary if using python - more compatible
#add option at start for default video options and default audio options
#discord_default_music("https://www.youtube.com/watch?v=P3MBQciFeHo")
