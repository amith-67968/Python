x=5
print(x)

def hello():
    global x
    x=4
    print(f"the local x is{x}")
    print("hello amith")

print(f"the global x is {x} ")
hello()
print(f"the global x is {x} ")