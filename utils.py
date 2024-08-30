from datetime import datetime
import time

def getToday():
    date = datetime.today()
    return date.strftime("%Y-%m-%d %H:%M:%S")


def startTime():
    return time.time()

