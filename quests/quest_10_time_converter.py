#!/usr/bin/python3
total_minutes = int(input("Enter total time in minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{total_minutes} minutes is equal to {hours} hour(s) and {minutes} minute(s).")
