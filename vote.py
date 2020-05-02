import requests
from datetime import datetime
import urllib3
import re
import random
import time



#GETS RID OF INSECUREREQUESTWARNING
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s = requests.Session()
new = 0

def clock():
    current = datetime.now()
    return(str(current) + " EST")
clock()


def get_proxies():
    global meek
    # COPY FILE PATH TO PROXIES HERE
    #ADJUST ACCORDINGLY
    text_file = open("/Users/Mac/Downloads/Proxies/proxies.json", "r")
    lines = text_file.readlines()
    meek = [item.replace('\n', '') for item in lines]
    text_file.close()
get_proxies()



pro = random.choice(meek)
meek.remove(pro)
proxy = {"http": 'http://' + pro}

#CHANGE LINK FOR YOUR SPECIFIC POLL
link = 'https://poll.fm/10111408'
#PDI ANSWER IS YOUR VOTE CHOICE
PDI_answer = '46414409'

head = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'referer': link,
        'Upgrade-Insecure-Requests': '1'
    }


def inform():
    global t_fixed
    global hidden_fixed
    global pz

    try:
        poll = s.get(link, headers=head, timeout=5, proxies=proxy, verify=False)
    except:
        print(clock(), ':: error, trying again')
    else:

        nounc = re.search("data-vote=\"(.*?)\"",poll.text).group(1).replace('&quot;','"')
        n = nounc.split(":")

        t_hidden = n[-4]
        t_fixed = t_hidden[0:-4]

        hidden = n[-1]
        hidden_fixed = hidden[1:-2]

        pz = re.search("type='hidden' name='pz' value='(.*?)'",poll.text).group(1)
        
inform()

while True:
    try:
        inform()
        link_me = 'https://poll.fm/vote?va=10&pt=0&r=1&p=10111408&a=' + PDI_answer + '%2C&o=&t=' + t_fixed + '&token=' + hidden_fixed + '&pz=' + pz
        vote = s.get(link_me, headers=head, timeout=5, proxies=proxy, verify=False)
        url = vote.url
    except:
        print(clock(), ':: error, trying again')
    else:
        if 'voted' in url:
            new += 1
            print(clock(), "::", 'New votes submitted = ' + str(new))
            #ADJUST TIMER INBETWEEN REQUESTS TO MAKE FASTER OR SLOWER
            time.sleep(5)
        else:
            print(clock(), ':: something went wrong')

