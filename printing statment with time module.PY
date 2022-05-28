#to print any statment with 2sec gap...

import time

localtime = time.asctime(time.localtime(time.time()))
print("Todays date & time is :",localtime)    #only for printing a prasent time

k =0
while(k<10):
    print("Stay at home & always wear a mask")
    k+=1
    time.sleep(2)