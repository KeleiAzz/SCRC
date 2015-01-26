__author__ = 'keleigong'
# coding: UTF-8
import base64
import sys
import codecs
from xml.etree.ElementTree import ElementTree


import xml.dom.minidom

tree = ElementTree()
tree.parse( '/Users/keleigong/Dropbox/Python/Project-SCRC/link_content_233.xml' ) # 从命令行指定 xml 文件

root = tree.getroot()
default_uid = 1

fp = codecs.open('/Users/keleigong/Dropbox/Python/Project-SCRC/xmltest.txt', 'w', 'utf8')

for row in root:
    data = {}
    for field in row:
        data[field.attrib.get('name')] = field.text

#        if data['post_type'] != 'post':
#            continue

    content = data['content']
    if content:
            # 如果有 COPY TO 任何格式提配错误，可以转换
            # content 为 base64 类型，导入后再修改回来
        content = base64.encodestring(content.encode('utf8')).strip()
        content = r"\r\n".join(content.splitlines())
#       content = content.replace('\n', r'\r\n')

# 写到文件： postgresql copy to/from 格式
''' fp.write('%s\t' % data['ID'])
    fp.write('%s\t' % default_uid)
    fp.write('%s\t' % data['post_title'])
    fp.write('%s\t' % content)
    fp.write('%s\t' % data['post_date'])
    fp.write('%s\n' % data['post_modified'])'''




#fp.write('\.')
#fp.close()










