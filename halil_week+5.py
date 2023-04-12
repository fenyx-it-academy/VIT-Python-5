telefon_listesi = {}
add_msg = "Kisi ekleme basari ile gerceklestirildi."
edit_msg = "Kisi duzenleme basari ile gerceklestirildi."
del_msg = "Kisi silme basari ile gerceklestirildi"
final_msg = "Islem sonlandiriliyor.."
liste = ["0", "1", "2", "3", "4", "5"]

while True:
    def kisi_ekle():
        while True:

            kisi = input(
                "Eklemek istediginiz isimi giriniz:\nCikmak icin 'q' ya basiniz ").title()
            if kisi == "Q":
                break
            numara = input("9 haneli Numara giriniz: (+31)")

            if len(numara) != 9 or not numara.isdigit():
                print("Yanlis yada eksik giris yaptiniz.\nLutfen tekrar deneyiniz..\n\n")
                continue

            telefon_listesi[kisi] = numara
            print(add_msg + "\n\n")

        return final_msg + "\n\n"

    def kisi_duzenle():

        while True:
            kisi = input(
                "Duzenlemek istediginiz ismi yaziniz:\nCikmak icin 'q' ya basiniz \n").title()
            if kisi == "Q":
                break
            if kisi not in telefon_listesi:
                print("Yanlis yada eksik giris yaptiniz.\nLutfen tekrar deneyiniz..\n\n")
                continue
            else:
                kisi_islem = input(f"""
            {kisi} ismini duzenlemek icin \t-1-
            \tsilmek icin\t-2- \n\n""")
            if kisi_islem == "1":
                yeni_kisi = input(f"{kisi} ismini duzenleyiniz: ").title()

                numara_yenileme = input(
                    "9 haneli Yeni numarayi giriniz : (+31)")

                if len(numara_yenileme) != 9 or not numara_yenileme.isdigit():
                    print(
                        "Hatali yada eksik giris yaptiniz lutfen tekrar giris yapiniz..\n\n")
                    continue
                else:
                    telefon_listesi[yeni_kisi] = numara_yenileme
                    del telefon_listesi[kisi]
                    print(edit_msg + "\n\n")
            elif kisi_islem == "2":
                del telefon_listesi[kisi]
                print(f"{kisi} kisisi basari ile silinmistir.")
        return final_msg + "\n\n"

    def kisi_silme():
        while True:
            kisi = input(
                "Silmek istediginiz ismi yaziniz.\nCikmak icin 'q' ya basiniz \n").title()
            if kisi == "Q":
                break

            if kisi not in telefon_listesi:
                print("Yanlis yada eksik giris yaptiniz.\nLutfen tekrar deneyiniz..\n\n")
                continue
            else:
                del telefon_listesi[kisi]
                print(del_msg + "\n")

        return final_msg + "\n\n"

    def kisi_arama():
        while True:
            kisi = input(
                "Aramak istediginiz ismi giriniz: \nCikmak icin 'q' ya basiniz\n").title()
            if kisi == "Q":
                break

            if kisi not in telefon_listesi:
                print("Yanlis yada eksik giris yaptiniz.\nLutfen tekrar deneyiniz..\n\n")
                continue
            else:
                print(
                    f"Aradiginiz kisi:\t{kisi}\nNumarasi: \t\t{telefon_listesi[kisi]}\n\n")

        return final_msg

    print("Telefon rehberi uylulamasina hosgeldiniz..")
    print("Yapmak istediginiz islemi seciniz\n")
    print("""
Kisi eklemek icin\t -1-
Kisi duzenlemek icin \t -2-
Kisi silmek icin \t -3-
Kisi aramak icin\t -4-
Tum liste \t\t -5-
Cikmak icin \t\t -0-        
        
        """)
    islem = input("--->:")
    if islem not in liste:
        print("Yanlis yada eksik giris yaptiniz.\nLutfen tekrar deneyiniz..\n\n")
        continue

    if islem == "0":
        print("Uygulamadan cikiliyor..")
        break

    elif islem == "1":
        print("Kisi ekleme menusu:\n")
        print(kisi_ekle())

    elif islem == "2":
        print("Kisi duzenleme menusu:\n")
        print(kisi_duzenle())

    elif islem == "3":
        print("Kisi silme menusu:\n")
        print(kisi_silme())

    elif islem == "4":
        print("Kisi arama menusu:\n")
        print(kisi_arama())

    elif islem == "5":
        print(telefon_listesi)
