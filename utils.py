from datetime import datetime

def getToday():
    date = datetime.today()
    return date.strftime("%Y-%m-%d %H:%M:%S")