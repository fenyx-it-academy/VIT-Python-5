"""
Telefon Rehberi Uygulaması
"""

contact_book = {
                "0123456789": {"name":"ali", "last_name":"Veli", "phone_number":"0123456789"},
                "0687093461": {"name":"ali", "last_name":"Jordan", "phone_number":"0687093461"},
                "0687093462": {"name":"can", "last_name":"Jobs", "phone_number":"0687093462"},
                "0687093463": {"name":"Leyla", "last_name":"Stone", "phone_number":"0687093463"},
                "0687093464": {"name":"Albert", "last_name":"Stein", "phone_number":"0687093464"},
                "0687093465": {"name":"Phoenix", "last_name":"Vogel", "phone_number":"0687093465"},
                "0687093466": {"name":"William", "last_name":"Wallace", "phone_number":"0687093466"},
                "0687093468": {"name":"Kobe", "last_name":"Bryant", "phone_number":"0687093468"},
                "0687093469": {"name":"Enes", "last_name":"Kanter", "phone_number":"0687093469"}
                }

#  Kişi Eklemek

def add_contact():
    """Kullanıcıdan aldığı Tel. numarasını Rehberde kontrol eder. 
    Yoksa kşinin diğer bilgilerini kullanıcıdan alarak rehbere ekleme yapar.
    Tel. No rehberde eşsizdir."""
    phone_number = input(f"Please enter 'Phone Number': ")
    while phone_number in contact_book.keys():
        print("Contact is already exists. Please add another contact") 
        phone_number = input(f"Please enter 'Phone Number': ")
            
    else:
        name = input(f"Please enter 'Name': ")
        last_name = input(f"Please enter 'Last Name': ")
        contact_book[phone_number] = {"name": name, "last_name": last_name, "phone_number":phone_number}
        add_another = input("Do you want to add another 'Contact'? \n Pres: 'Y' or 'N': ").upper().strip()           
        if add_another == "Y":
            add_contact()
                   

# Kişi Düzenlemek
  
def organize():
    contact_name = input(f"Please enter 'Contact Name': ")
    for key, value in contact_book.items():
        for sub_values in value.values():
            if contact_name == sub_values:
                choise = input("Please choose one option. 'D' for 'Delete', 'U' for 'Update'  ").upper().strip()
                if choise == "D":                 
                    contact_book.pop(key)              
                    return contact_book.values()        
                else:
                    print("Please enter new updated contact information:  ")
                    phone_number = input(f"Please enter 'Phone Number': ")
                    name = input(f"Please enter 'Name': ")
                    last_name = input(f"Please enter 'Last Name': ")
                    contact_book[key].update({"name": name, "last_name": last_name, "phone_number":phone_number})
                    # return print(contact_book.values())        
    return print(f"{contact_name} is not in contacts ") 
    
# Kşi Silmek

def delete_contact():
    contact = input(f"Please enter Contact 'Name', 'Last Name' or 'Phone Number':  ")
    for key, value in contact_book.items():
        for sub_key, sub_value  in value.items():
            if contact == sub_value:
                contact_book.pop(key)
                return contact_book.values()   

# Kişi Aramak

def choose_contact():
    contact = input(f"Please enter Contact 'Name', 'Last Name' or 'Phone Number':  ")
    for key, value in contact_book.items():
        for sub_key, sub_value  in value.items():
            if contact == sub_value:
                return print(key, "->", value)
    return print("key doesn't exist")           

# Kişilerin Dökümünü almak

def look_contacts():
    for key, value in contact_book.items():
        print(f"Info for Phone Number #{key} is:   ")
        for sub_key, sub_value in value.items():
            print(sub_key, "->", sub_value)
        print('-'*35)  

#Ana Menu
             
def call_main_menu():
    global main_menu
    main_menu = input(""" Choose a menu:
                'Add' a contact Press -> '1';
                'Update' a contact Press -> '2';
                'Delete' a contact Press -> '3';
                'Find' a contact Press -> '4';
                'Look' all Contacts Press-> '5';
                for 'Exit' Press -> 'Any key' ;
                  """)
    return main_menu


while True:
    # call_main_menu()

    if main_menu == "1":
        add_contact()        
                    
    elif main_menu == "2":
        organize()        
            
    elif main_menu == "3":
        delete_contact()        
        
    elif main_menu == "4":
        choose_contact()
        
    elif main_menu == "5":
        look_contacts()
        
    else:
        print("Good by!")
        break
       
