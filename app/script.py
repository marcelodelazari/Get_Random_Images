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
    imgur_req = Request("https://i.imgur.com/Y4Beqvb", headers={'User-Agent': 'Mozilla/5.0'})
    return render_template('index.html', random_img="https://i.imgur.com/r7QL273.png")


if __name__ == "__main__":
    app.run()
