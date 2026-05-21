import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(1,100):
#     os.mkdir(f"data/Day{i}")

# for i in range(1,100):
#     os.rename(f"data/Tutorial{i}",f"data/Tutorial {i}")


folders=os.listdir()
print(folders)