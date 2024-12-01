import requests as rt
import datetime as dt
import os.path

def get_input(**kwargs):
    # get day and month
    today = dt.datetime.today()
    day = kwargs['day'] if ('day' in kwargs) else today.day
    year = kwargs['year'] if ('year' in kwargs) else today.year   
    
    # do we have a session cookie?
    if not os.path.isfile('./aoc_sessioncookie'):
        print('For the first run, you will need to enter your session cookie.\nTo find out, click on "get your puzzle input", open developer tools, go to the network tab, reload the page, click on any request, go to the cookies tab, and copy the long hexadecimal number (without quotes).\nIf you don\'t understand, try googling for a guide.\nIf you get it wrong, just delete the file "aoc_sessioncookie" in the current folder.')
        cookie = input('\nPaste it here: ')
        cookiefile = open('./aoc_sessioncookie', 'w')
        cookiefile.write(cookie)
        cookiefile.close()
     
    # get the cookie
    cf = open('./aoc_sessioncookie', 'r')
    cookie = cf.read()
    cf.close()
    
    # set session cookie
    s = rt.Session()
    s.cookies.set('session', cookie, domain='.adventofcode.com')

    # make request
    r = s.get('https://adventofcode.com/' + str(year) + '/day/' + str(day) + '/input')
    if r.status_code != 200:
        if r.status_code == 500:
            print('error: there was a server error. maybe your session cookie is wrong? (500)')
        elif r.status_code == 404:
            print('error: looks like there is no problem on the given date. (404)')
        else:
            print('error: http code ' + str(r.status_code))
        return None
        
    return r.text
    