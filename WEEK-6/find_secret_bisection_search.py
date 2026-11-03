from secret_data import secret_year

guesses = 0
low = 0
high = 2026
guess = (low + high) // 2

while guess != secret_year:
    if guess < secret_year:
        low = guess + 1
    elif guess > secret_year:
        high = guess - 1
    
    guess = (low + high) // 2
    guesses += 1

print(f"Gizli yıl bulundu: {guess}. Toplam tahmin sayısı: {guesses}")