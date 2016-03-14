from bikeProject.models import Counter
from time import sleep

def fillDB(i):
    c = Counter(currentCount=i)
    c.save()
    i = i + 1
    sleep(.5)
    fillDB(i)
