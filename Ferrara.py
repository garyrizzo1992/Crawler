from bs4 import BeautifulSoup
import responses
import urllib2
import sqlite3
import re

def returnsourcecode(url):
    page = urllib2.urlopen(url)

    soup = BeautifulSoup(page, "html.parser")
    return soup;

def getmenulinks():

    returnsourcecode("http://www.ferraramalta.com/")

    url = "http://www.ferraramalta.com/"
    page = urllib2.urlopen(url)

    soup = BeautifulSoup(page, "html.parser")

    # Finding the menu tag for level 1
    all_links = soup.find('ul', class_='level1')

    # Finding the links inside the menu items
    all_links2 = all_links.findAll('a', attrs={'href': re.compile("^http://")})

    # SQLite databse wordflow
    try:
      conn = sqlite3.connect("Ferrara")
      c = conn.cursor()
      c.execute("CREATE TABLE MenuLinks (""Title"",""URL"")")
      print "Table MenuLinks created successfully"
    except Exception as ex:
       print ex

    # Printing & inserting
    for link in all_links2:
       try:
          print link.text + " " + link.get("href")
          print "Inserting row:"
          c.execute("INSERT INTO  MenuLinks (""Title"",""URL"") VALUES(?,?)", (link.text, link.get("href")))
          conn.commit()
          print "Inserted"
       except Exception as ex:
          print ex
    return;



#getmenulinks()

soup = returnsourcecode("http://www.ferraramalta.com/index.php?main_page=index&cPath=65_77")

#print soup.prettify()

all_links = soup.find("table", {"class": "tabTable"})

print all_links

for row in all_links.findall("tr"):
    col = row.findall("td")

    print col


# print soup.prettify()
