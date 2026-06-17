from datetime import datetime, timedelta

time = "05:00 am"


def addTime(time,hour,minute):
    calcTime = datetime.strptime(time,"%I:%M %p") + timedelta(hours=hour,minutes=minute)
    return datetime.strftime(calcTime,"%I:%M %p")














