import random

def getRandomLink():
    num = random.randrange(100000, 999999)
    site = "http://prnt.sc/" + str(num)
    return site