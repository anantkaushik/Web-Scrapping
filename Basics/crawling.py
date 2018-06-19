import bs4 as bs #importing beautiful soup 4
import urllib.request #importing request
import re #importing Regular Expression
import random #importing random

def getLinks(pageURL): #funtion to open the link and fetching other links from that page
    url = urllib.request.urlopen('http://challengers.pythonanywhere.com'+pageURL) #opening the link
    code = bs.BeautifulSoup(url,'lxml') #converting into the BeautifulSoup Object
    return code.findAll("a", href = re.compile("^(/)((?!:).)*$"))  #returning the list of all the links which start from "/"

links = getLinks("/") #calling the getLinks function
while len(links) > 0: 
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"] #selecting the random link from the list of links. 
    print(newArticle)#printing the selected link
    links = getLinks(newArticle) #calling the getLinks function