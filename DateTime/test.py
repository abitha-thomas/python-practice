import datetime

liveTime=datetime.datetime.now()
print(liveTime)
print(liveTime.year)
print(liveTime.month)
print(liveTime.hour)
print(liveTime.day)
print(liveTime.minute)
print(liveTime.second)
print(liveTime.microsecond)

print(liveTime.strftime("%M"))


birthday = datetime.datetime(2005,3,10)
age_days = liveTime - birthday
age_years = liveTime.year - birthday.year
print(age_days)
print(age_years)

print(liveTime + datetime.timedelta(days=1))
print(liveTime + datetime.timedelta(days=1))
print(liveTime + datetime.timedelta(days=1,hours=2))
print(liveTime + datetime.timedelta(days=1,hours=2))
