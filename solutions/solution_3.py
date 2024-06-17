n=int(input("enter the number of seconds that have passed since the beginning of the day:"))
hours=n//3600
minutes=(n%3600)//60
seconds=(n%3600)
Time=(hours,":", minutes,":", seconds)
print(Time)
