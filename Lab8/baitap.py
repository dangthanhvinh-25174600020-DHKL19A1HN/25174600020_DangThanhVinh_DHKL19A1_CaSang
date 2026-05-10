#Bài 8.1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print("Các cặp số nguyên tố sinh đôi < 1000:")

for i in range(2, 1000):
    if is_prime(i) and is_prime(i + 2):
        print((i, i + 2))
#Bài 8.2
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n = int(input("Nhập n: "))
print("Giai thừa:", factorial(n))
#Bài 8.3
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def permutation(n, r):
    return factorial(n) // factorial(n - r)
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
n = int(input("Nhập n: "))
r = int(input("Nhập r: "))
print("Hoán vị:", permutation(n, r))
print("Tổ hợp:", combination(n, r))
#Bài 8.4
def cubesum(n):
    total = 0
    for digit in str(n):
        total += int(digit) ** 3
    return total
n = int(input("Nhập số: "))

print("Tổng lập phương các chữ số:", cubesum(n))
#Bài 8.5
def cubesum(n):
    total = 0
    for digit in str(n):
        total += int(digit) ** 3
    return total
def isArmstrong(n):
    return n == cubesum(n)
print("Các số Armstrong từ 1 đến 1000:")
for i in range(1, 1001):
    if isArmstrong(i):
        print(i)
#Bài 8.6
def sumPdivisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total
n = int(input("Nhập số: "))
print("Tổng ước số thực sự:", sumPdivisors(n))
#Bài 8.7
def sumPdivisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total
def isAmicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if isAmicable(a, b):
    print("Là cặp số Amicable")
else:
    print("Không phải cặp số Amicable")
#Bài 8.8
arr = list(map(int, input("Nhập mảng: ").split()))
even = list(filter(lambda x: x % 2 == 0, arr))
odd = list(filter(lambda x: x % 2 != 0, arr))
print("Số chẵn:", even)
print("Số lẻ:", odd)
#Bài 8.9
arr = list(map(int, input("Nhập mảng: ").split()))
cube_list = list(map(lambda x: x ** 3, arr))
print("Danh sách lập phương:")
print(cube_list)
#Bài 8.10
arr = list(map(int, input("Nhập mảng: ").split()))
even_cube = list(
    map(lambda x: x ** 3,
        filter(lambda x: x % 2 == 0, arr))
)
odd_square = list(
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 != 0, arr))
)
print("Lập phương số chẵn:")
print(even_cube)
print("Bình phương số lẻ:")
print(odd_square)