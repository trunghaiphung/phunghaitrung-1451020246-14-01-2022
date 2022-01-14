print("câu a")
a = 'Hải'
b = 'Trung'
print(a, b)
print(len(a),len(b))
print("câu B")

def totalDigitsOfNumber(n):
    total = 0
    while (n > 0):
        total = total + n % 10
        n = int(n / 10)
    return total
n = int(35)
print("Tổng các chữ số của", n, "là", totalDigitsOfNumber(n))
