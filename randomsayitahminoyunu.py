#Tutulan Sayıyı Bulma (Random Bir Sayı)
import random #Random kütüphanesini ekliyoruz
randomsayi=random.randint(1,100) #randomsayi değişkenine 1-100 arası rastgele değer atmasını sağlıyoruz
tahminim=0

while tahminim!=randomsayi: #döngüyü başlatım doğru sayı girilene kadar sürdürüyoruz
    tahminim=int(input("1-100 Arasında Sayı Giriniz:"))
    if tahminim<randomsayi:
        print("Daha büyük bir sayı girin:")
    elif tahminim>randomsayi:
        print("Daha küçük bi sayı girin:")
    else:
        print("Bravo doğru sayıyı bildiniz!")
