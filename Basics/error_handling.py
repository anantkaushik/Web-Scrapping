import bs4 as bs #importing beautiful soup 4
import urllib.request #importing request
from urllib.error import HTTPError
from urllib.error import URLError

try: #checking for exceptions
    url = urllib.request.urlopen('http://challengers.pythonanywhere.com/').read() #reading the url

except HTTPError as e: #catch the HTTPError
    print(e)

except URLError as e: #catch the URLError
    print("URL not found")

else:#if there wa no exceptions raised. This block will execute
    code = bs.BeautifulSoup(url,'lxml') #converting into the Beautiful Soup object.

    try:#checking for exceptions
        x = code.nonExistingTag.Attribute #fetching information from tag(here i try to fetch info from non-existing tag to raise error)
    except AttributeError as e: #catch the AttributeError
        print("Tag Not Found")
    else:#if there wa no exceptions raised. This block will execute
        print(x) #printing the data inside the tag