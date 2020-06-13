import requests, json
from bs4 import BeautifulSoup


def research_website(url='https://vnexpress.net'):
    ## Append the prefix for url if needed
    if 'http://' not in url or 'https://' not in url:
        url = 'http://' + url

    ## Check if getting source is possible
    try:
        response    = requests.get(url)
    except:
        print("Cannot get the source of the given website url!")
        return 
    
    ##
    source      = BeautifulSoup(response.content, 'lxml')

    ## Get all the div
    content     = ''
    for div in source.find('body').find_all('div'):
        content+= ' ' + div.text.strip().replace('\n',' ').lower()
        
    ##
    content     = content.replace('\xa0', ' ')
    content     = content.replace('\n', ' ')
    content     = list(filter(None, content.split(' ')))

    ##
    histogram   = {}
    for item in content:
        if item.isalpha():
            try:
                histogram[item]+=1
            except:
                histogram[item]=1
    
    return histogram