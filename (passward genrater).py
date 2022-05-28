#"""""""""STRONG PASSWARD GENRATER"""""""

print("\n\n\t\t\t\t\t\t\tWelcome, to passward genrater machine ")

import random

lst = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-~*?><|;:[]"
passwardlen = int(input("\n\t\t\t\t\t\t\tEnter a length of your passward: "))

a= "".join(random.sample(lst, passwardlen))

if passwardlen>=10:
    print("\n\t\t\t\t\t\t\tThis is your passward: ", a)
    print("\n\t\t\t\t\t\t\tGreat; Your passward is VERY STRONG 100%")

elif passwardlen>=6 and passwardlen<10:
    print("\n\t\t\t\t\t\t\tThis is your passward: ", a)
    print("\n\t\t\t\t\t\t\tYour passward is STRONG 80%")

elif passwardlen>=4 and passwardlen<6:
    print("\n\t\t\t\t\t\t\tThis is your passward: ", a)
    print("\n\t\t\t\t\t\t\tYour passward is WEEK 50%")

elif passwardlen>=0 and passwardlen<4:
    print("\n\t\t\t\t\t\t\tThis is your passward: ", a)
    print("\n\t\t\t\t\t\t\tOpps; Your passward is VERY WEEK 25%")