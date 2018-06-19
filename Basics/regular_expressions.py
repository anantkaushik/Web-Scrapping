import bs4 as bs #importing beautiful soup 4
import urllib.request #importing request
import re #importing Regular Expression

url = urllib.request.urlopen('http://challengers.pythonanywhere.com/').read() #reading the url

code = bs.BeautifulSoup(url,'lxml') #converting into the Beautiful Soup object.

for link in code.find_all("a",{"href":re.compile(".com")}): #iterating the list conatining all the anchor tags whose "href" contains ".com".
    print(link) #printing the anchor tags