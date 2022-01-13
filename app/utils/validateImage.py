from urllib.request import Request, urlopen

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