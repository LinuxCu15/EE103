# Part 1: Recap
# User Input, Type Casting, & String Formatting
std_num = int(input("Öğrenci numaranızı girin: "))
print(f"Hello, my student number is {std_num}!")

# String Manipulation & Slicing
name_lower = 'name'
print(name_lower.upper())
print(name_lower[::-1])

# User Input with Floats & Basic Arithmetic
this_year = 2026
s_year = str(this_year)
first_two = float(s_year[:2])
last_two = float(s_year[2:])
mysum = first_two + last_two
print(f"{mysum:.2f}")

if mysum == 46:
    print("Correct")
else:
    print("Wrong")