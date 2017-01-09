from bs4 import BeautifulSoup
import responses
import urllib2
import re

url = "http://www.ferraramalta.com/"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page,"html.parser")


print soup.title.string


all_links = soup.find('ul', class_='level1')

all_links2 = all_links.findAll('a', attrs={'href': re.compile("^http://")})

#print str(all_links.prettify())

for link in all_links2:
        try:
            print link.text
            print link.get("href")
        except Exception as ex:
            print ex

#print soup.prettify()