# Part 6: Float Precision Explanation
x = 0
for i in range(10):
    print(x)
    x = x + 0.1

# Açıklama: Bilgisayarlar ondalıklı sayıları ikili (binary) sistemde saklar. 
# 0.1 sayısı ikili sistemde sonsuz devirli bir kesir olduğu için toplama 
# işlemlerinde ufak bir donanımsal hassasiyet/yuvarlama kaybı yaşanır ve 1 yerine 0.99999... çıktısı alınır.