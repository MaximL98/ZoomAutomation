import urllib.request


def have_internet():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=2)
        return True
    except:
        return False

