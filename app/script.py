from flask import Flask, render_template
from urllib.request import Request, urlopen
import random
app = Flask(__name__)


@app.route('/')
def index():

    num = random.randrange(100000, 999999)
    site = "http://prnt.sc/" + str(num)
    req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
    html = str(urlopen(req).read())

    img_class = "twitter:image:src"
    img_class_index = html.index(img_class)
    img_link_ini = img_class_index + len(img_class) + 11
    img_link_end = img_link_ini + html[img_link_ini:].index('"')
    img_link = html[img_link_ini:img_link_end]

    return render_template('index.html', random_img=img_link)

if __name__ == "__main__":
    app.run()