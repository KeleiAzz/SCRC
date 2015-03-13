from urllib import urlopen
from BeautifulSoup import BeautifulSoup

text = urlopen('https://www.google.com.hk/#newwindow=1&c2coff=1&safe=active&q=scrape').read()
soup = BeautifulSoup(text)

jobs = set()
for header in soup('h3'):
    links = header('a', 'reference')
    if not links: continue
    link = links[0]
    jobs.add('%s (%s)' % (link.string, link['href']))

print '\n'.join(sorted(jobs, key=lambda s: s.lower()))