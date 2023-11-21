# weight = [0,0,0]
# sum=0
# for i in range(1,4):
#     weight[i] = int(input("{} student weight is : ".format(i)))
#     sum += weight[i]
# print("The sum of the weight is ",sum)

a = [[0,0,0],[0,0,0],[0,0,0]]
b = []
c = []
for i in range (3):
    for j in range (3):
        a[i][j] = int(input())
for i in range (3):
    for j in range (3):
        b[i][j] = int(input())
for i in range (3):
    for j in range (3):
        c[i] = a[i]+b[i]