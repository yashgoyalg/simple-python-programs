#Simple calculator
#(Desgin a calculator which will correctly solve all int type problems...)

print("Enter 1st Number")
num1 = float(input())
print('Enter 2nd Number')
num2 = float(input())
print('so What you Want?'+'+,-,/,%,*')
num3 =input()

if num3=='*' :
    Mult=num1*num2
    print(Mult)
elif num3 == '+':
    plus=num2+num1
    print(plus)
elif num3 == '/':
    Dev=num2/num1
    print(Dev)
elif num3 == '-':
    Dev=num2-num1
    print(Dev)
elif num3 == '%':
    percent=num2%num1
    print(percent)
else:
    print("Error! Please check your input")