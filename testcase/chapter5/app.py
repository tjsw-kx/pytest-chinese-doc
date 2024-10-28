from urllib import request

def get(url):
    r= request.urlopen(url)
    return r.read().decode('utf-8')
