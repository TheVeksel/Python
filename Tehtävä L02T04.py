from datetime import datetime
current_datetime = datetime.now()
name = input('Anna etunimesi:')
date = int(input('Syntymävuotesi:'))
nowdate = (current_datetime.year)
print("Hei", name, "olet", nowdate - date)