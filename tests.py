import urllib.request


def have_internet():
    # trying to open url
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=2)
        # if successful, return True meaning there is internet connection
        return True
    except:
        # else, there is no internet connection and False is returned
        return False

