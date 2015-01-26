__author__ = 'keleigong'

# coding: UTF-8
import base64

import codecs
from xml.etree.ElementTree import ElementTree
import xml.dom.minidom

dom=xml.dom.minidom.parse('/Users/keleigong/Dropbox/Python/Project-SCRC/link_content_233.xml')

root = dom.documentElement

print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE
print root.ATTRIBUTE_NODE



root = dom.documentElement

cc=dom.getElementsByTagName('content')

length = []

for i in range(len(cc)):
    length.append(len(cc[i].firstChild.data))

length2 = []
for i in range(len(cc)):
    temp=cc[i].firstChild.data
    temp = base64.b64decode(temp).strip()
    temp = r"\r\n".join(temp.splitlines())

    cc[i].firstChild.data = temp
    length2.append(len(cc[i].firstChild.data))
#print c1.firstChild.data


'''f=file('/Users/keleigong/Dropbox/Python/Project-SCRC/content_233.xml','w')
dom.writexml(f,'',' ','\n','utf-8')
f.close()'''


print 'end'