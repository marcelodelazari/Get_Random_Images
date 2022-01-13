from flask import Flask, render_template
from urllib.request import Request, urlopen
import random

def getRandomLink():
    num = random.randrange(100000, 999999)
    site = "http://prnt.sc/" + str(num)
    return site

def validateImage(imgur_link):
    if "prntscr" in imgur_link:
        print(imgur_link)
        return False

    imgur_req = Request(imgur_link, headers={'User-Agent': 'Mozilla/5.0'})
    imgur_html = str(urlopen(imgur_req).read())
    print(imgur_html)
    if 'content="https://www.facebook.com/imgur">  <script src=' in imgur_html:
        print(imgur_link)
        return False
    return True

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    found_image = False
    while not found_image:

        site = getRandomLink()
        req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
        print(req)
        asd = "Tudo certo."
        try:
            html = str(urlopen(req).read())

            img_class = "twitter:image:src"
            img_class_index = html.index(img_class)
            img_link_ini = img_class_index + len(img_class) + 11
            img_link_end = img_link_ini + html[img_link_ini:].index('"')
            img_link = html[img_link_ini:img_link_end]

            imgur_link = img_link[:len(img_link) - 4]
            print(imgur_link)
            found_image = validateImage(imgur_link)
            print("Found image." if found_image else "Image is crashed.")
        except Exception as e:
            asd = e

    return render_template('index.html', random_img=img_link, error_message=asd)


if __name__ == "__main__":
    app.run()
