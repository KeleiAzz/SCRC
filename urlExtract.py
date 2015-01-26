__author__ = 'keleigong'
#-*-coding=utf-8-*-
import urllib2,urllib
import json
import openpyxl as ox
#seachstr = 'apple sustainability'
seachstr2 = 'apple supplier'
seachstr3 = 'apple supplier labor'

companyList = ['apple', 'nike', 'lenovo', 'deere', 'amazon']
keyword = ['sustainability','supplier','supplier labor','supplier portal','procurement','supplier code of conduct','vendor portal']
date = '2012..2014'

urlextract = ox.Workbook()
sheet = urlextract.create_sheet(0,'sheet1')

all_URL = []

file=open('result.txt','w')
Row = 1
for company in companyList:
    for key in keyword:
        searchstr = company+ ' ' + key + ' ' + date
        for x in xrange(2):
            print "page:%s"%(x+1)
            page = x*10 #page = x

            url = ('https://ajax.googleapis.com/ajax/services/search/web'
                          '?v=1.0&q=%s&rsz=8&start=%s') % (urllib.quote(searchstr),page)
            try:
                request = urllib2.Request(
                url, None, {'Referer': 'http://www.google.com'})
                response = urllib2.urlopen(request)

            # Process the JSON string.
                results = json.load(response)
                infoaaa = results['responseData']['results']
            except Exception,e:
                print e
            else:
                for minfo in infoaaa:
                    if minfo['url'][4] == 's':
                        url = minfo['url'][8:-1]
                    else:
                        url = minfo['url'][7:-1]
                    if url not in all_URL:
                        print url
                        file.write(url+'\n')
                        sheet.cell(row = Row, column = 1).value = company
                        sheet.cell(row = Row, column = 2).value = key
                        sheet.cell(row = Row, column = 3).value = minfo['url']
                        Row += 1
                        all_URL.append(url)

file.close()
urlextract.save('urlextract.xlsx')