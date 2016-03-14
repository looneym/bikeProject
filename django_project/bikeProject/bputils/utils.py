def fillDB(i):
    c = Counter(currentCount=i)
    c.save()
    i = i + 1
    sleep(.5)
    fillDB(i)
