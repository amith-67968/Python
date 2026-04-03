num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
choice=int(input("\n" \
"1.Addition(+)\n" \
"2.Subtraction(-)\n" \
"3.Multipllication(*)\n" \
"4.Division(/)\n" \
"5.Power(^)\n"
"Enter your choice:"))
if(choice==1):
    print(num1+num2)
if(choice==2):
    print(num1-num2)
if(choice==3):
    print(num1*num2)
if(choice==4):
    print(num1/num2)
if(choice==5):
    print(num1**num2)
