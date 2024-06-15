'''
question -> find the date 45 days before today 

'''

from datetime import datetime, timedelta

today = datetime.today()

print(today)

days_before = today - timedelta(days=45)

print(days_before)


# formated date
print("Today's date:", today.strftime("%Y-%m-%d"))
print("Date 45 days before today:", days_before.strftime("%Y-%m-%d"))