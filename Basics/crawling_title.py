import bs4 as bs #importing beautiful soup 4
import urllib.request #importing request
import re #importing Regular Expression

pages = set()
def getLinks(pageURL): #funtion to open the link and fetching other links from that page
    url = urllib.request.urlopen('http://challengers.pythonanywhere.com'+pageURL) #opening the link
    code = bs.BeautifulSoup(url,'lxml') #converting into the BeautifulSoup Object
    try:
        print("Title of the page is "+ code.title.text) #fetching and printing the title of the page
    except AttributeError as e: #if title tag doesn't exist.
        print("Title not found") 
    for l in  code.findAll("a", href = re.compile("^(/)((?!:).)*$")):  #traversing the list of all the links which start from "/"
        if l.attrs["href"] not in pages: #if link is not traversed
            pages.add(l.attrs["href"]) #adding link to the set "pages"
            getLinks(l.attrs["href"]) #traversing the link

links = getLinks("/") #calling the getLinks function
