# Part 9: Binary Conversion with Tolerance Range for 0.1
target = 0.1
f = target
total_val = 0.0
factor = 0.5
binary_res = "."

for _ in range(30):
    f *= 2
    if f >= 1:
        binary_res += "1"
        total_val += factor
        f -= 1
    else:
        binary_res += "0"
    
    factor /= 2
    
    if abs(total_val - target) < 0.00001:
        break

print("0.1'in tolerans aralığındaki binary değeri:", binary_res)