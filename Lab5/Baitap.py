#Bài 5.1
n = int(input("Nhập số nguyên dương: "))
binary = ""
while n > 0:
    binary = str(n % 2) + binary
    n //= 2
print("Dạng nhị phân:", binary)
#Bài 5.2
str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
found = False
for length in range(1, len(str1) + 1):
    for i in range(len(str1) - length + 1):
        sub = str1[i:i + length]
        if sub in str2:
            print("Chuỗi con chung ngắn nhất:", sub)
            found = True
            break
    if found:
        break
if not found:
    print("Không có chuỗi con chung.")
#Bài 5.3
text = input("Nhập chuỗi: ")
keyword = input("Nhập từ khóa: ")
# Tìm vị trí xuất hiện
index = text.find(keyword)
while index != -1:
    print("Từ khóa xuất hiện tại vị trí:", index)
    index = text.find(keyword, index + 1)
# Đếm tần suất từ
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

max_word = max(freq, key=freq.get)
print("Từ xuất hiện nhiều nhất:", max_word)
print("Số lần:", freq[max_word])
#Bài 5.4
text = input("Nhập chuỗi: ")
number_str = ""
for ch in text:
    if ch.isdigit():
        number_str += ch
number = int(number_str)
print("Số sau khi xử lý:", number)
is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print("Là số nguyên tố")
else:
    print("Không phải số nguyên tố")
#Bài 5.5
str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")
result = ""
max_len = max(len(str1), len(str2))
for i in range(max_len):
    if i < len(str1):
        result += str1[i]

    result += "-"
    if i < len(str2):
        result += str2[i]
    result += "-"
print("Chuỗi trộn:", result)
#Bài 5.6
text = input("Nhập chuỗi: ")
special = {}
for ch in text:
    if not ch.isalnum() and ch != " ":
        special[ch] = special.get(ch, 0) + 1
length = len(text)
for ch, count in special.items():
    percent = (count / length) * 100
    print(f"Ký tự '{ch}': {count} lần ({percent:.2f}%)")
#Bài 5.7
text = input("Nhập chuỗi: ")
upper = 0
lower = 0
digit = 0
special = 0
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1
print("Chữ hoa:", upper)
print("Chữ thường:", lower)
print("Chữ số:", digit)
print("Ký tự đặc biệt:", special)
#Bài 5.8
text = input("Nhập chuỗi: ")
if len(text) <= 10:
    print("Chuỗi phải lớn hơn 10 ký tự")
else:
    print("Từ vị trí 2 đến 8:", text[2:9])
    print("5 ký tự từ vị trí 5:", text[5:10])
    print("3 ký tự cuối:", text[-3:])
    print("Chữ hoa:", text.upper())
    print("Chữ thường:", text.lower())
    print("Đảo ngược:", text[::-1])
#Bài 5.9
str1 = input("Nhập chuỗi ban đầu: ")
str2 = input("Nhập chuỗi mục tiêu: ")
if abs(len(str1) - len(str2)) <= 1:
    print("Có thể chuyển đổi bằng thêm/xóa/thay thế ký tự")
else:
    print("Khó chuyển đổi")
#Bài 5.10
text = input("Nhập chuỗi: ")
result = text.replace(" ", "")
print("Chuỗi sau khi xóa khoảng trắng:", result)