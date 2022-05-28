#code 1

# name = "YASH"
# strl = name.lower()
# print(name)
# print(strl)

#code 2

# a= [10,20,(30,40)]
# print("Orginal list A:",a)
# print(id(a))

#code 3

# a= [10,20,(30,40)]
# print("Orginal list A:",a)
# print(id(a))
# print(type(a))
# print(len(a))

# n = len(a)
# for i in range(n):
#     if type(a[i]) is tuple:
#         if len(a[i])>1:
#             m = len(a[i])
#             for j in range(m):
#                 print(i,j,a[i][j])
#         else:
#             print(i, a[i])

#code 3 list comprehension 

# list = []
# for i in range(20):
#     if(i%2==1):
#         list.append(i)
# print(list)
# list1 = [i  for i in range(20) if i%2==0]
# print("new list", list1)

#code 4

# list = [0,1,2,3,4,5,6,7,8,9,10]
# new_list = []
# for i in list:
#     new_list.append(i)

# print("new list",new_list)

#