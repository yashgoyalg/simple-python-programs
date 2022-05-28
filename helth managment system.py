#********************Helth Mannagement System*********************

import datetime
def date():
    hour= datetime.datetime.now()
    return hour
def firstStep():

    print("1: write","2: rettrive")
    a= int(input("="))

    if a==1:
        print("1: food","2: exercise")
        b= int(input("="))

        if b==1:
            print("1: harry", "2: rohan","3:vishal")
            c= int(input("="))

            if c==1:
                f = open("harryF.txt","w")
                print("OK!, write somthing")
                d = int(input("="))
                f.write(d)
                print("item added succesfully")
                hour= datetime.datetime.now()
                f.close()
            elif c==2:
                f = open("rohanF.txt","w")
                print("OK!, write somthing")
                e = int(input("="))
                f.write(e)
                print("item added succesfully")
                hour= datetime.datetime.now()
                f.close()
            elif c==3:
                f = open("vishalF.txt","w")
                print("OK!, write somthing")
                g = int(input("="))
                f.write(g)
                print("item added succesfully")
                hour= datetime.datetime.now()
                f.close()

        elif b==2:
            print("1: harry", "2: rohan","3:vishal")
            c= int(input("="))

            if c==1:
                f = open("harryE.txt","w")
                print("OK!, write somthing")
                d = int(input("="))
                f.write(d)
                print("item added succesfully")
                hour= datetime.datetime.now()
                f.close()
            elif c==2:
                f = open("rohanE.txt","w")
                print("OK!, write somthing")
                e = int(input("="))
                f.write(e)
                print("item added succesfully")
                hour= datetime.datetime.now()
                f.close()
            elif c==3:
                f = open("vishalE.txt","w")
                print("OK!, write somthing")
                g = int(input("="))
                f.write(g)
                print("item added succesfully")
                hour= datetime.datetime.now()
                f.close()
    if a==1:
        print("1: food","2: exercise")
        b= int(input("="))

        if b==1 or b== 2:
            print("1: harry", "2: rohan","3:vishal")
            c= int(input("="))

            if c==1:
                f= open("harryF.txt", "r")
                f1= open("harryE.txt", "r")
                print(f"[{date()}]"+ "food=",end="\t")
                print(f.read())
                print(f"[{date()}]"+ "exercise=",end="\t")
                print(f1.read())
                print("finished")
                f.close()
                f1.close()

            elif c==2:
                f= open("rohanF.txt", "r")
                f1= open("rohanE.txt", "r")
                print(f"[{date()}]"+ "food=",end="\t")
                print(f.read())
                print(f"[{date()}]"+ "exercise=",end="\t")
                print(f1.read())
                print("finished")
                f.close()
                f1.close()

            elif c==3:
                f= open("vishalF.txt", "r")
                f1= open("vishalE.txt", "r")
                print(f"[{date()}]"+ "food=",end="\t")
                print(f.read())
                print(f"[{date()}]"+ "exercise=",end="\t")
                print(f1.read())
                print("finished")
                f.close()
                f1.close()
        def restart():
            while True:
                print("do u want to check again")
                reply = input("=")
                if reply == "yes":
                    a()
                elif reply == "no":
                    print("thank u")
                    break
        a()
        restart()


