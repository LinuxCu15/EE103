# Part 8: Fraction to Binary Conversion (0.375)
f = 0.375
binary_fraction = "."

for _ in range(5):
    f *= 2
    integer_part = int(f)
    binary_fraction += str(integer_part)
    f = f - integer_part
    if f == 0:
        break

print("0.375 kesrinin binary karşılığı:", binary_fraction)