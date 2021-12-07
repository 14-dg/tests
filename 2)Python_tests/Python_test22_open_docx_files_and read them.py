# import docx

# def getText(filename):
#     doc = docx.Document(filename)
#     fullText = []
#     for para in doc.paragraphs:
#         fullText.append(para.text)
#     return '\n'.join(fullText)

# print(getText("demo.docx"))


##########################
#don't know if this works#
##########################

# def para2text(p):
#     rs = p._element.xpath('.//w:t')
#     return u" ".join([r.text for r in rs])

# print(para2text("demo.docx"))


###########################
#don't know what this does#
###########################


# # add
# import re
# import sys

# # add
# def remove_hyperlink_tags(xml):
#     if (sys.version_info > (3, 0)):
#         xml = xml.decode('utf-8')
#     xml = xml.replace('</w:hyperlink>', '')
#     xml = re.sub('<w:hyperlink[^>]*>', '', xml)
#     if (sys.version_info > (3, 0)):
#         xml = xml.encode('utf-8')
#     return xml
    
# # update
# def parse_xml(xml):
#     """
#     Return root lxml element obtained by parsing XML character string in
#     *xml*, which can be either a Python 2.x string or unicode. The custom
#     parser is used, so custom element classes are produced for elements in
#     *xml* that have them.
#     """
#     root_element = etree.fromstring(remove_hyperlink_tags(xml), oxml_parser)
#     return root_element

