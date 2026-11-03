# Part 7: Decimal to Binary Conversion (13)
decimal = 13
orijinal_sayi = decimal
remainders = ""

while decimal > 0:
    remainders += str(decimal % 2)
    decimal = decimal // 2

binary_result = remainders[::-1]
print(f"{orijinal_sayi} sayısının binary karşılığı:", binary_result)