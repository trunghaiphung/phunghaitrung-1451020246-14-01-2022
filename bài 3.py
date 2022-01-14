print("câu a")
a = 'Phùng '
b = 'Hải '
c = 'Trung'
print(a, b, c)

print("câu b")
def isThuanNghich(n):
    str1 = str(n)
    str2 = str1[::-1]
    if (str1 == str2):
        return True
    else:
        return False
print(len(a),len(b),len(c))
d = 645546
n = int (d)
print("Tổng các chữ số của", n, "là", isThuanNghich(n))
m = int(d)
print("Tổng các chữ số của", m, "là", isThuanNghich(m))
print("Tổng các chữ số của", n, "là", isThuanNghich(n))