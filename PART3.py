# Part 3: Unique Letters with String Accumulator and Loop
s = "abcabc"
unique_letters = ""

for char in s:
    if char not in unique_letters:
        unique_letters += char

print(f"'{s}' kelimesindeki benzersiz harf sayısı:", len(unique_letters))