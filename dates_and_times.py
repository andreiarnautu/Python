from datetime import datetime
delta = datetime.now() - datetime(1999, 10, 20)
print(str(delta.days))

current_date = datetime.now()
print(current_date.strftime("%d-%m-%Y %H:%M"))
print(current_date.day)
print(delta.day)