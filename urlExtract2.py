__author__ = 'keleigong'
#import sys # Used to add the BeautifulSoup folder the import path
import urllib2 # Used to read the html document
from bs4 import BeautifulSoup
if __name__ == "__main__":
    ### Import Beautiful Soup
    ### Here, I have the BeautifulSoup folder in the level of this Python script
    ### So I need to tell Python where to look.
    #sys.path.append("./BeautifulSoup")


    ### Create opener with Google-friendly user agent
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    ### Open page & generate soup
    ### the "start" variable will be used to iterate through 10 pages.
    for start in range(0,2):
        url = "http://www.google.com/search?q=supplier+site:apple.com&start=" + str(start*10)
        page = opener.open(url)
        soup = BeautifulSoup(page)

        ### Parse and find
        ### Looks like google contains URLs in <cite> tags.
        ### So for each cite tag on each page (10), print its contents (url)

        for cite in soup.findAll('cite'):
            print cite.text