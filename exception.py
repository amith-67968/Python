a=input("Enter the number:")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{a}X {i}={int(a)*i}")
except:
    print("error")
finally:
    print("end of program")