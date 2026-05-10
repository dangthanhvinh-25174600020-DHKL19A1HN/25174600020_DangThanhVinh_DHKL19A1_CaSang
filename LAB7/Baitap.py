#Bài 7.1\
N = int(input("Nhập N: "))
cube_dict = {}
for x in range(1, N + 1):
    cube_dict[x] = x ** 3
print(cube_dict)
#Bài 7.2
n = int(input("Nhập số sinh viên: "))
students = {}
for i in range(n):
    name = input("Tên sinh viên: ")
    score = float(input("Điểm: "))
    if score >= 8.5:
        grade = "A"
    elif score >= 7:
        grade = "B"
    elif score >= 5.5:
        grade = "C"
    elif score >= 4:
        grade = "D"
    else:
        grade = "F"
    students[name] = grade
print("Kết quả xếp loại:")
for name, grade in students.items():
    print(name, ":", grade)
#Bài 7.3
students = {
    "An": "A",
    "Bình": "B",
    "Lan": "A",
    "Minh": "C",
    "Hoa": "B"
}
count = {}
for grade in students.values():
    count[grade] = count.get(grade, 0) + 1
print("Thống kê học lực:")
for grade, total in count.items():
    print(grade, ":", total)
#Bài 7.4
text = input("Nhập đoạn văn: ")
# Làm sạch dữ liệu
text = text.lower()
for ch in ",.!?;:":
    text = text.replace(ch, "")
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Tần suất từ:")
for word, count in freq.items():
    print(word, ":", count)
#Bài 7.5
text = input("Nhập đoạn văn: ")
text = text.lower()
for ch in ",.!?;:":
    text = text.replace(ch, "")
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
max_word = max(freq, key=freq.get)
min_word = min(freq, key=freq.get)
print("Từ xuất hiện nhiều nhất:")
print(max_word, ":", freq[max_word])
print("Từ xuất hiện ít nhất:")
print(min_word, ":", freq[min_word])
#Bài 7.6
inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstone"],
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}
# Thêm pocket
inventory["pocket"] = ["seashell", "strange berry", "lint"]
# Cập nhật gold
inventory["gold"] += 50
print(inventory)
#Bài 7.7
inventory = {
    "backpack": ["xylophone", "dagger", "bedroll", "bread loaf"]
}
# Sắp xếp
inventory["backpack"].sort()
# Xóa vật phẩm
inventory["backpack"].remove("dagger")
print(inventory["backpack"])
#Bài 7.8
stock = {
    "Táo": 5,
    "Cam": 3,
    "Chuối": 4
}
price = {
    "Táo": 10000,
    "Cam": 15000,
    "Chuối": 8000
}
total = 0
print("HÓA ĐƠN")
for item in stock:
    cost = stock[item] * price[item]
    total += cost
    print(f"{item}: {stock[item]} x {price[item]} = {cost}")
print("Tổng tiền:", total)
#Bài 7.9
inventory = {
    "Táo": 10,
    "Cam": 8,
    "Chuối": 15
}
sold = {
    "Táo": 3,
    "Cam": 2
}
for item in sold:
    if item in inventory:
        inventory[item] -= sold[item]
print("Tồn kho sau giao dịch:")
for item, quantity in inventory.items():
    print(item, ":", quantity)
#Bài 7.10
warehouse = {"Táo", "Cam", "Chuối", "Xoài", "Nho"}
customer_cart = {"Táo", "Nho"}
not_bought = warehouse - customer_cart
print("Sản phẩm chưa được mua:")
print(not_bought)
