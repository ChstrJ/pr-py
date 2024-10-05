from datetime import datetime
import time

def getToday():
    date = datetime.today()
    return date.strftime("%Y-%m-%d %H:%M:%S")

def startTime():
    return time.time()

def log(filename = "logs.txt", data=""):
    
    with open(filename, 'a') as f:
        f.write(f"{data} ---- {getToday()} \n")
        
        
def getAllReviewers():
    
    return [
        "justin-qt",
        "berns-qt",
        "christian-qt",
        "prang-qt",
        "daniellamnl-qt",
        "kurt-qt",
        "arriantolentino"
        "chnvrla",
        "khristinesophia14"
    ]
    
def getVuReviewers():
    
    return [
        "charlesartillero",
        "Seth-ITW",
        "kurt-qt",
        "chnvrla",
        "khristinesophia14"
        "berns-qt",
        "daniellamnl-qt",
    ]
