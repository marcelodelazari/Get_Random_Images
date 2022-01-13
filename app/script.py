from urllib.request import Request, urlopen
import flask
site="http://prnt.sc/654321"
req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
html = str(urlopen(req).read())

img_class = "twitter:image:src"
img_class_index = html.index(img_class)
img_link_ini = img_class_index + len(img_class) + 11
img_link_end = img_link_ini + html[img_link_ini:].index('"')
img_link = html[img_link_ini:img_link_end]
print(img_link)
