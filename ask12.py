import datetime
from datetime import date

now = datetime.datetime.now()

input_date = input("Δώστε μια ημερομηνία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ")

day_date = int(input_date[0:2])
month_date = int(input_date[3:5])
year_date = int(input_date[6:10])

a = datetime.date(now.year, now.month, now.day)
b = datetime.date(year_date, month_date, day_date)

delta = b - a

hours = delta.days * 24
minutes = hours * 60
seconds = minutes * 60
    
print(delta.days, "days", hours, "hours", minutes, "minutes", seconds, "seconds", "until the given date")

if month_date==1 or month_date==3 or month_date==5 or month_date==7 or month_date==8 or month_date==10 or month_date==12 :
    print ("Ο μήνας έχει 31 μέρες")
elif month_date==2 and year_date%4==0:
    print ("O μήνας έχει 29 μέρες")
elif month_date==2 and year_date%4!=0:
    print ("O μήνας έχει 28 μέρες")
elif month_date==4 or month_date==6 or month_date==9 or month_date==11:
    print ("Ο μήνας έχει 30 μέρες")
