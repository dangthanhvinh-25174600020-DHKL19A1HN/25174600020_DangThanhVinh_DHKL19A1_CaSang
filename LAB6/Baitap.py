#Bai 6.1
n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    x = int(input(f"Phần tử {i + 1}: "))
    arr.append(x)
sum_even = 0
sum_odd = 0
for x in arr:
    if x % 2 == 0:
        sum_even += x
    else:
        sum_odd += x
print("Tổng số chẵn:", sum_even)
print("Tổng số lẻ:", sum_odd)
#Bai 6.2
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n
n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Phần tử {i + 1}: ")))
print("Các số nguyên tố:")
for x in arr:
    if is_prime(x):
        print(x, end=" ")
print("\nCác số hoàn hảo:")
for x in arr:
    if is_perfect(x):
        print(x, end=" ")
#Bai 6.3
n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(float(input(f"Phần tử {i + 1}: ")))
print("Giá trị lớn nhất:", max(arr))
print("Giá trị nhỏ nhất:", min(arr))
#Bai 6.4
n = int(input("Nhập n: "))
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
print("Dãy Fibonacci:")
print(fib[:n])
#Bài 6.5
prime_list = [
    x for x in range(2, 100)
    if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
]
print("Các số nguyên tố nhỏ hơn 100:")
print(prime_list)
#Bài 6.6
n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Phần tử {i + 1}: ")))
diff = arr[1] - arr[0]
is_arithmetic = True
for i in range(1, n - 1):
    if arr[i + 1] - arr[i] != diff:
        is_arithmetic = False
        break
if is_arithmetic:
    print("Dãy là cấp số cộng")
else:
    print("Dãy không phải cấp số cộng")
#Bài 6.7
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
matrix = []
for i in range(m):
    row = list(map(int, input(f"Hàng {i + 1}: ").split()))
    matrix.append(row)
total = 0
for row in matrix:
    total += sum(row)

print("Tổng ma trận:", total)
#Bài 6.8
m = int(input("Số hàng ma trận A: "))
n = int(input("Số cột ma trận A: "))
A = []
for i in range(m):
    row = list(map(int, input(f"Hàng A{i + 1}: ").split()))
    A.append(row)
p = int(input("Số cột ma trận B: "))
B = []
for i in range(n):
    row = list(map(int, input(f"Hàng B{i + 1}: ").split()))
    B.append(row)
# Khởi tạo ma trận kết quả
C = [[0 for _ in range(p)] for _ in range(m)]
for i in range(m):
    for j in range(p):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]
print("Tích hai ma trận:")
for row in C:
    print(row)
#Bài 6.9
n = int(input("Nhập kích thước ma trận vuông: "))
matrix = []
for i in range(n):
    row = list(map(int, input(f"Hàng {i + 1}: ").split()))
    matrix.append(row)
# Chuyển vị
transpose = [[matrix[j][i] for j in range(n)] for i in range(n)]
print("Ma trận chuyển vị:")
for row in transpose:
    print(row)
# Kiểm tra đối xứng
if matrix == transpose:
    print("Ma trận đối xứng")
else:
    print("Ma trận không đối xứng")
#Bài 6.10
n = int(input("Nhập cấp ma trận: "))
if n != 2:
    print("Chương trình chỉ hỗ trợ ma trận 2x2")
else:
    matrix = []
    for i in range(2):
        row = list(map(float, input(f"Hàng {i + 1}: ").split()))
        matrix.append(row)
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    det = a * d - b * c
    if det == 0:
        print("Ma trận không khả nghịch")
    else:
        inverse = [
            [d / det, -b / det],
            [-c / det, a / det]
        ]
        print("Ma trận nghịch đảo:")
        for row in inverse:
            print(row)