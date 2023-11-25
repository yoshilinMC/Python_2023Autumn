a = [[1,2,4],[3,5,7],[2,4,9]]
for i in range(3):
    for j in range(3):
        print("{}".format(a[j][i]),end=" ")
        if j == 2:
            print("\n")
print("O(n*n)")