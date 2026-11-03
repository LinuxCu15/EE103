from secret_data import secret_year

guesses = 0
for guess in range(2027): 
    guesses += 1
    if guess == secret_year:
        print(f"Gizli yıl bulundu: {guess}. Toplam tahmin sayısı: {guesses}")
        break