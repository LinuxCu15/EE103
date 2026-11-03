year_str = input("What year is this? ")
year = int(year_str)

digit_sum = 0
for digit in str(year):
    digit_sum += int(digit)

result_division = digit_sum / len(str(year))
print(f"Toplamın basamak sayısına bölümü: {result_division}")

x = 0.1
y = 0.2
result = x + y

print(f"Sonuç tam olarak 0.3'e eşit mi? (result == 0.3): {result == 0.3}")
print(f"Sonuç yeterince yakın mı? (0.3-1e-4 <= result <= 0.3+1e-4): {0.3 - 1e-4 <= result <= 0.3 + 1e-4}")