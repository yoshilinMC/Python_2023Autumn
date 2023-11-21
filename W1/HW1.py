def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True


n = int(input())
if is_prime(n):
    print(n, "是否為質數 : True")
else:
    print(n, "是否為質數 : False")