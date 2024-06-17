numberhr=input("enter the number of hours that have passed since the beginnin oof the day between 0-11hrs:")
minutes=input("enter the number of minutes that have  passed since the beginnign of the hour 0to59mins")
seconds=input("enter the number of seconds past the minute 0-59secs")
mins=int(minutes)//5
ang=int(numberhr)-mins
print((ang/12)*360)
