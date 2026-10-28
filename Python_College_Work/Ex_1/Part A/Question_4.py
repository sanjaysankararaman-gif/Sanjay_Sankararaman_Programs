time_in_seconds = int(input("Enter time in seconds:"))

hours = time_in_seconds // 3600 #1 hr has 3600 seconds

reminder = time_in_seconds % 3600 #calculates the number of seconds passed in the hour

minutes = reminder // 60 #1 minute has 60 seconds

seconds = reminder % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
