import time
hour=int(time.strftime("%H"))
if hour>=5 and hour<12:
    print("Good Morning")
elif(hour>=12 and hour<16):
    print("Good afternoon")
elif(hour>=16 and hour<19):
    print("Good evening")
else:
    print("Good night")