from secret_data import secret_number

epsilon = 0.01
step = 0.01
guess = 0.0
guesses = 0

while abs(guess**2 - secret_number) >= epsilon and guess**2 <= secret_number:
    guess += step
    guesses += 1

print(f"Approximation - Toplam tahmin sayısı: {guesses}")
if abs(guess**2 - secret_number) < epsilon:
    print(f"Yaklaşık karekök: {guess}")
else:
    print("Hesaplama başarısız oldu (step boyutu büyük kalmış olabilir).")