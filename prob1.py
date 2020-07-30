# print the following output
#Enter the number limit : 7
# 2
# 4
# 6
# 8
# 10
# 12
# 14

numberlimit=int(input("enter a number "))
for i in range(numberlimit):
    i=(i+1)*2
    print(i)

