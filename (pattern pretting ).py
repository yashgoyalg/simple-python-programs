i=0

print("pettern printing")

num= int(input("How many rows you want to print: "))

print("Enter 1 0r 0")

bool_val = input("1 for true or 0 for false: ")

if bool_val== "1":
    for i in range(0,num+1):
        print("*"*i)

elif bool_val== "0":
    for i in range(num,0,-1):
        print("*"*i)
