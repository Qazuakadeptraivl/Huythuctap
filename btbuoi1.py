"""
    bài tập:
    - cho biết kiểu của các giá trị sau: -50, 4.98908, .5, 4+5j
    - định nghĩa 2 biến num1, num2 có cùng giá trị 1
    - nhập vào tên và tuổi và hiển thị ra màn hình, cách nhau bởi dấu phẩy
    - nhập vào 1 số nguyên, số thực, chuỗi và in các giá trị của chúng trên các dòng riêng biệt
"""

# Cau1
s = -50
print('Kieu gia tri cua S la: ',type(s))

d = 4.98908
print('Kieu du lieu cua d la: ',type(d))

f = .5
print('Kieu du lieu cua f la: ',type(f))

g = 4+5j
print('Kieu du lieu cua g la: ',type(g))

s = -50
d = 4.98908
f = .5
g = 4+5j
print("Cac kieu du lieu lan luot cua {},{},{} la",type({},{},{}).format(s, d, f, g))


# Cau2
num1 = 1
num2 = 1


# Cau3
user = input("Nhap ten + tuoi")
print(" Ten va tuoi ")

# Cau4
user = input("Nhap 1 so bat ky:")
print(user(type(user)))











































































