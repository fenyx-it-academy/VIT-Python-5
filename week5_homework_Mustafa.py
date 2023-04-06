# VIT-Python-5
# Telefon Rehberi Uygulaması
# Bu program, kullanıcıların telefon rehberlerindeki kişileri yönetmelerine ve aramalarına olanak tanır. 
# Program, Python sözlüklerini kullanarak verileri depolar.


rehber={'AD Soyad': '1234556789','AAA bbbb': '987654321'} # 

# kişi_ekle()
# Bu fonksiyon, kullanıcıdan bir kişi adı ve telefon numarası alarak telefon rehberine ekler.
def kisi_ekle():
    ad=input("Rehbere eklemek istediginiz adi giriniz:")
    tel=input("Rehbere eklemek istediginiz numarayi giriniz:")
    rehber.update({ad:tel})
    print(f"{ad} ,{tel} rehbere kaydedildi")
    
    
    
# kişi_düzenle()
# Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur. Ardından, kullanıcıya mevcut verileri güncelleme veya silme seçenekleri sunar.
def kisi_duzenle():
    ad=input("Rehberede degistirmek istediginiz adi giriniz:")
    print(f"{ad} ,{rehber[ad]} duzenlenecek")
    del rehber[ad]
    ad=input("Rehbere eklemek istediginiz adi giriniz:")
    tel=input("Rehbere eklemek istediginiz numarayi giriniz:")
    rehber.update({ad:tel})
    print(f"{ad} ,{tel} rehbere kaydedildi")
    
    
# kişi_sil()
# Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur ve siler.
def kisi_sil():
    ad=input("Silmek istediginiz adi giriniz:")
    print(f"{ad} ,{rehber[ad]} silinecek...")
    print(f"{ad} ,{rehber[ad]} silindi")
    del rehber[ad]
    
    
    
# kişi_arama()
# Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur ve ekrana görüntüler.
def kisi_arama():
    ad=input("Aramak istediginiz adi giriniz:")
    print(f"{ad} ,{rehber[ad]} aranacak.")
  

while True:
    print("\nTelefon Rehberi Uygulaması")
    print("1 - Yeni kişi ekle")
    print("2 - Kişi düzenle")
    print("3 - Kişi sil")
    print("4 - Kişi arama")
    print("5 - Çıkış")
    secim = input("Seçiminizi girin: ")
    if secim == "1":
        kisi_ekle()
        print(rehber)
        
    elif secim == "2":
        kisi_duzenle()
      
    elif secim == "3":
        kisi_sil()

    elif secim == "4":
        kisi_arama()

    elif secim == "5":
        break
    else:
        print("Geçersiz seçim.")

print(rehber)

# ===Hackerrank===
# 1 ==============
# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the
# result of float division, a / b.
# No rounding or formatting is necessary.
# Example
# a=3
# • The result of the integer division 3//5= 0. • The result of the float division is 3/5 = 0.6.
# b=5
# Print:
# 0 0.6


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)

