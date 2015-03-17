__author__ = 'keleigong'
import scrape
import pdfminer


def write_to_txt(res):
    file = open('res_fq', 'w')
    for i in res.keys():
        file.write('URLs appear %d times \n' % i)
        for url in res[i]:
            file.write('  ' + url + '\n')
    file.close()


def download_content(url):
    s = scrape.Session()
    s.go(url)
    d = s.doc
    file = open('url_content', 'w')
    file.write(unicode(d.text).encode('ascii', 'ignore'))
    file.close()
    print 'Download finished'


def pdf_to_csv(filename):
    from cStringIO import StringIO
    from pdfminer.converter import LTChar, TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfparser import PDFParser
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfpage import PDFPage

    class CsvConverter(TextConverter):
        def __init__(self, *args, **kwargs):
            TextConverter.__init__(self, *args, **kwargs)

        def end_page(self, i):
            from collections import defaultdict

            lines = defaultdict(lambda: {})
            for child in self.cur_item._objs:  # <-- changed
                if isinstance(child, LTChar):
                    (_, _, x, y) = child.bbox
                    line = lines[int(-y)]
                    line[x] = child._text.encode(self.codec)  #<-- changed

            for y in sorted(lines.keys()):
                line = lines[y]
                self.outfp.write(";".join(line[x] for x in sorted(line.keys())))
                self.outfp.write("\n")

    # ... the following part of the code is a remix of the
    # convert() function in the pdfminer/tools/pdf2text module
    rsrc = PDFResourceManager()
    outfp = StringIO()
    device = CsvConverter(rsrc, outfp, codec="utf-8", laparams=LAParams())
    # becuase my test documents are utf-8 (note: utf-8 is the default codec)


    fp = open(filename, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)
    parser.set_document(doc)
    # doc.set_parser(parser)
    # doc.initialize('')

    interpreter = PDFPageInterpreter(rsrc, device)
    pagenos = set()
    rotation = 0
    i = 1
    for page in PDFPage.get_pages(fp, pagenos):
        page.rotate = (page.rotate + rotation) % 360
        outfp.write("START PAGE %d\n" % i)
        interpreter.process_page(page)
        outfp.write("END PAGE %d\n" % i)
        i += 1

    # for i, page in enumerate(doc.get_pages()):
    # outfp.write("START PAGE %d\n" % i)
    #     if page is not None:
    #         interpreter.process_page(page)
    #     outfp.write("END PAGE %d\n" % i)

    device.close()
    fp.close()
    return outfp.getvalue()


print pdf_to_csv('Apple_Progress_Report_2015.pdf').replace(';', '')
# download_content('http://www.scpr.org/news/2014/12/02/48409/lausd-ipads-federal-agents-confiscate-documents-re/')