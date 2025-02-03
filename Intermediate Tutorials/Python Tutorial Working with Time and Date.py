"""
Python Tutorial 17: Working with Time and Date

This tutorial covers various ways to work with dates and times in Python using the datetime module.
It includes:
- Getting the current date and time
- Formatting dates and times
- Parsing date strings
- Performing arithmetic on dates
- Working with time zones
- Converting timestamps
"""

from datetime import datetime, date, time, timedelta, timezone
import time as time_module

# 1. Getting the Current Date and Time
now = datetime.now()
print("Current Date and Time:", now)
print("Current Date:", now.date())
print("Current Time:", now.time())

# 2. Formatting Dates and Times
formatted_date = now.strftime("%Y-%m-%d")  # YYYY-MM-DD
formatted_time = now.strftime("%H:%M:%S")  # HH:MM:SS
formatted_datetime = now.strftime("%A, %d %B %Y, %I:%M %p")  # Full format
print("Formatted Date:", formatted_date)
print("Formatted Time:", formatted_time)
print("Formatted Datetime:", formatted_datetime)

# Common formatting codes:
# %Y - Year (4 digits)
# %y - Year (last 2 digits)
# %m - Month (01-12)
# %B - Month name
# %d - Day (01-31)
# %A - Weekday name
# %H - Hour (24-hour)
# %I - Hour (12-hour)
# %p - AM/PM
# %M - Minutes (00-59)
# %S - Seconds (00-59)

# 3. Parsing Date Strings
date_str = "2024-02-03 15:45:30"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed Datetime:", parsed_date)

# 4. Date Arithmetic
future_date = now + timedelta(days=10)
past_date = now - timedelta(weeks=3)
print("10 Days from Now:", future_date)
print("3 Weeks Ago:", past_date)

difference = future_date - now
print("Time Difference in Days:", difference.days)

# 5. Working with Time Zones
utc_now = datetime.now(timezone.utc)
print("UTC Time:", utc_now)

# Converting UTC to local timezone
ist_offset = timedelta(hours=5, minutes=30)
ist_timezone = timezone(ist_offset)
ist_now = utc_now.astimezone(ist_timezone)
print("IST Time:", ist_now)

# 6. Timestamps
current_timestamp = time_module.time()
print("Current Timestamp:", current_timestamp)

datetime_from_timestamp = datetime.fromtimestamp(current_timestamp)
print("Datetime from Timestamp:", datetime_from_timestamp)

# 7. Extracting Components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# 8. Creating Specific Date and Time Objects
specific_date = date(2024, 12, 25)
specific_time = time(14, 30, 45)
specific_datetime = datetime(2024, 12, 25, 14, 30, 45)
print("Specific Date:", specific_date)
print("Specific Time:", specific_time)
print("Specific Datetime:", specific_datetime)

# 9. Measuring Execution Time
start_time = time_module.perf_counter()
time_module.sleep(1.5)  # Simulate a process taking 1.5 seconds
end_time = time_module.perf_counter()
execution_time = end_time - start_time
print("Execution Time:", execution_time, "seconds")
