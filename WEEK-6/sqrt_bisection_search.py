from secret_data import secret_number

epsilon = 0.01
low = 0.0
high = max(1.0, secret_number)
guess = (low + high) / 2.0
guesses = 0

while abs(guess**2 - secret_number) >= epsilon:
    if guess**2 < secret_number:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2.0
    guesses += 1

print(f"Bisection - Toplam tahmin sayısı: {guesses}")
print(f"Hesaplanan karekök: {guess}")