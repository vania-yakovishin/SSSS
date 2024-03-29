import datetime
date_time = datetime.datetime(2023, 10, 12, hour=12, minute=38, second=53, microsecond=352)
print(f"object datetime - {date_time}")
print(f"type  - {type(date_time)}")
print("----------------------------------")
print(f"object datetime - {date_time.date()}\n type  - {type(date_time.date())} ")
print("----------------------------------")
print(f"object datetime - {date_time.time()}\n type  - {type(date_time.time())} ")
print("----------------------------------")
date_now = datetime.datetime.now()
print(date_now)
print("----------------------------------")
delta = datetime.timedelta(days=3, hours=3, weeks=3)
print(f"delta= {delta}\ntype - {type(delta)}")
print("----------------------------------")
print(date_now + delta)
print("----------------------------------")
print(date_now - delta)