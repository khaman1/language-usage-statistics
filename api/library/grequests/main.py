from fake_useragent import UserAgent
import grequests

def grequests_get(url):
    headers             = {"User-Agent": "Mozilla/6.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    response            = grequests.get(url,headers=headers)
    response            = grequests.map([response])[0]

    return response

def grequests_get_all(url_list):
    headers             = {'User-Agent':str(UserAgent().chrome)}
    rs                  = (grequests.get(u,headers=headers) for u in url_list)

    return grequests.map(rs)