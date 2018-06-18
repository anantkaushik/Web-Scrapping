import bs4 as bs #importing beautiful soup 4
import urllib.request #importing request

url = urllib.request.urlopen('http://challengers.pythonanywhere.com/').read() #reading the url

code = bs.BeautifulSoup(url,'lxml') #converting into the Beautiful Soup object.

print(code.p) #printing the first paragraph with its html tag.

print(code.p.text) #print the text present inside the first paragraph tag.

print(code.p.string) #same as "code.p.text" but only works when paragraph tag does not contain any child tag.

print(code.find_all('p')) #return the list of all the paragraphs tag present on the webpage.

for link in code.find_all('a'): #iterating all the anchor tag 
    print(link.get('href')) #fetching link from the anchor tag.