# # f=open('myfile2.txt','w')

# # text=f.write("hiii")
# # print(f)
# # f.close()

# with open('myfile.txt','a') as  f:
#     f.write("heyy")

f=open('myfile.txt','r')
while True:
    line=f.readline()
    print(line,type(line))
    if not line:
        break