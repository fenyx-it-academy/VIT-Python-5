"""

Telefon Rehberi Uygulaması
Bu program, kullanıcıların telefon rehberlerindeki kişileri yönetmelerine ve aramalarına olanak tanır.
Program, Python sözlüklerini kullanarak verileri depolar.

Özellikler

Yeni kişi ekleme
Kişi düzenleme
Kişi silme
Kişi arama
Fonksiyonlar
Programınız aşağıdaki fonksiyonlardan oluşabilir:

kişi_ekle()
Bu fonksiyon, kullanıcıdan bir kişi adı ve telefon numarası alarak telefon rehberine ekler.

kişi_düzenle()
Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur.
Ardından, kullanıcıya mevcut verileri güncelleme veya silme seçenekleri sunar.

kişi_sil()
Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur ve siler.

kişi_arama()
Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur ve ekrana görüntüler.
"""

#Telefon Rehberi Uygulamasi
#  Boş bir telefon defteri tanımlayın
phone_book = {}
    
# Telefon rehberini gosterir.

def look():
    print("***Telefon Rehberi***")
    if phone_book == {}:
        print("Kayitli numara yok! ")

    for item in phone_book:
        print(item + ": " + phone_book[item])
       

#  Yeni bir kişi ekleme işlevi
def add_person():
    name = input("isim girin  : ")
    number = input("Telefon no girin : ")
    phone_book[name] = number
    print("\n Kişi başarıyla eklendi!")
    

#  Bir kişiyi düzenleme işlevi
  
def person_edit():
    name = input("Guncellenecek ismi yaz  : ")
    if name in phone_book:
        print("Gucellecek numara:", phone_book[name])
        new_name = input("Yeni isim girin  (güncel tutmak için boş bırakın): ")
        if new_name != name :
            phone_book[new_name] = name
            print("\nKişi başarıyla guncellendi!")
        else:
            print("\nKisi bulunamadi!!")

        new_number = input("Yeni numara gir (güncel tutmak için boş bırakın): ")
        if new_number !="" :
            phone_book[new_name] = new_number
            print("Yeni numara basariyyal guncellendi!!")
        else:
            print("Numara guncellenemedi!")
    else:
        print("Kayit bulunamadi!")

        
    
#  Bir kişiyi silme işlevi
def person_delete():
    name = input("Silinecek kişinin adını girin  : ")
    if name in phone_book:
        del phone_book[name]
        print("Kişi başarıyla silindi!")
    else:
        print("Kisi bulunamadi!!")

#   Bir kişiyi arama işlevi
def person_search():
    name = input("Aranacak kişinin adını girin  : ")
    if name in phone_book:
        print(name, ":", phone_book[name])
    else:
        print("Kisi bulunamadi!!")

#  Ana program döngüsü 
while True:
    print()
    print("**Rehber Secenekleri**")
    print("1. Kisi ekleme")
    print("2. Kisi duzenleme")
    print("3. Kisi silme")
    print("4. Kisi arama")
    print("5. Rehber")
    print("6. Cikis")
    print("*********************\n")


    choice = (input("Bir islem seciminiz(1 ile 6 arasinda) : "))

    if choice == '1':
        add_person()
    elif choice == '2':
        person_edit()
    elif choice == '3':
        person_delete()
    elif choice == '4':
        person_search()
    elif choice == '5':
        look()    
    elif choice == '6':
        print("Rehberden Ciktiniz")
        break
    else:
        print("Yanlis secenek (1 ile 6 arasinda) Lutfen tekrar deneyin!!!")
