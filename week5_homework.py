# Telefon Rehberi Uygulaması
# Bu program, kullanıcıların telefon rehberlerindeki kişileri yönetmelerine ve aramalarına olanak tanır. 
# Program, Python sözlüklerini kullanarak verileri depolar.

# Özellikler

# kişi_ekle()
# Bu fonksiyon, kullanıcıdan bir kişi adı ve telefon numarası alarak telefon rehberine ekler.

# kişi_düzenle()
# Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur. 
# Ardından, kullanıcıya mevcut verileri güncelleme veya silme seçenekleri sunar.

# kişi_sil()
# Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur ve siler.

# kişi_arama()
# Bu fonksiyon, kullanıcıdan bir kişi adı alarak telefon rehberindeki kişiler listesinde bu kişiyi bulur ve ekrana görüntüler.

contacts = {
    "CAFER" : 344,
    "ÖMER" : 305,
    }

def kisi_ekle():
    name = input("Name : ").upper()
    if name in contacts:
        print("Already have contact")        
    else:
        number = input("Number : ")
        contacts[name] = number
        print(f" {name} added successfully.")

def kisi_arama():
    
    name = input("Name : ").upper()
    if name in contacts:
        print(f"""
        NAME      NUMBER

        {name} \t  {contacts[name]}
        """)
    else:
        print("The name not found")
        



def kisi_sil(name):
    contacts.pop(name)


def kisi_düzenle():
    name = input("Enter the name  : ").upper()
    if name in contacts:

        print(f"""
        NAME      NUMBER

        {name} \t  {contacts[name]}
        """)
        edit = int(input("""
        1 --- Edit
        2 --- Delete

        Choose one of the above (number) :"""))
        if edit == 1:
            edit = int(input("""
            1 --- Rename 
            2 --- Edit Number
            
            Choose one of the above (number) :"""))
            if edit == 1:
                name1 = input("Enter new name : ").upper()
                contacts[name1] = (contacts.get(name))
                contacts.pop(name)
            elif edit == 2:
                number = int(input("Enter new number :"))
                contacts.update({name : number})     

        else:
            print(name, "is deleted.")
            kisi_sil(name)
            
    else:
        print("Name not found")


while True:

    question = int(input("""
    1 --- Contacts
    2 --- Find
    3 --- Add
    4 --- Edit / Delete
    5 --- Exit
    
    Choose one of the above (number) : """))

    if question == 1:
        for i,j in contacts.items():
            print(f"{i} \t {j} ")
    elif question == 2:
        kisi_arama()
    elif question == 3:
        kisi_ekle()
    elif question == 4:
        kisi_düzenle()
    else:
        print("Exiting contacts...")
        break
