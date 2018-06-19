import bs4 as bs #importing beautiful soup 4
import urllib.request #importing request

url = urllib.request.urlopen('http://challengers.pythonanywhere.com/').read() #reading the url

code = bs.BeautifulSoup(url,'lxml') #converting into the Beautiful Soup object.

print(code.find("a",{"href":"/login"}).parent) #print the parent tag

for child in code.find("nav",{"id":"nav"}).children: #iterating the list conatining all the child elements of nav tag.
    print(child) #Printing the child