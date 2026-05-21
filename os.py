import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(1,100):
    os.mkdir(f"data/Day{i}")