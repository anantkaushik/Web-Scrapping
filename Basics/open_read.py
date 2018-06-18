import bs4 as bs #importing beautiful soup 4
import urllib.request #importing request

url = urllib.request.urlopen('http://challengers.pythonanywhere.com/').read() #reading the url

code = bs.BeautifulSoup(url,'lxml') #converting into the Beautiful Soup object.

print(code) #printing the source code