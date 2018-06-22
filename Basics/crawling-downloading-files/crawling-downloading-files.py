import bs4 as bs #importing beautiful soup 4
import urllib.request #importing request
import os #importing os
from urllib.error import HTTPError #importing http error

downloadDIrectory = "download"
baseURL = "http://challengers.pythonanywhere.com"
#function to get the absoluute url
def getAbsoluteURL(baseURL,source):
    if source.startswith("http://www."):
        url = "http://"+source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://"+source
    else:
        url = baseURL + "/" +source
    if baseURL not in url:
        return None
    return url

#function to set the download path
def getDownloadedPath(baseURL,absoluteURL,downloadDIrectory):
    path = absoluteURL.replace("www.","")
    path = path.replace(baseURL,"")
    path = downloadDIrectory + path
    directory = os.path.dirname(path)
    print(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

url = urllib.request.urlopen('http://challengers.pythonanywhere.com').read() #reading the url
code = bs.BeautifulSoup(url,'lxml') #converting into the Beautiful Soup object.
downloadList = code.findAll(src=True) #image list
for download in downloadList:
    try:
        fileURL = getAbsoluteURL(baseURL,download["src"])
        if fileURL is not None:
            urllib.request.urlretrieve(fileURL,getDownloadedPath(baseURL,fileURL,downloadDIrectory))
    except HTTPError as e: #catch the HTTPError
        print(e)