import os
Kitaplar = []

def main_menu():
    while True:
        os.system("clear")
        print()
        print("Kütüphane Uygulamasına Hoşgeldiniz!")
        print("-------------------------------------------")
        print("[1]. Yönetici Girişi")
        print("[2]. Kullanıcı Girişi")
        print("[3]. Çıkış")
        print("-------------------------------------------")

        secenek1 = input("Seçiminizi Yapın. (1/2/3): ")

        print("-------------------------------------------")


        if secenek1 == "1":
            admin_menu()
        elif secenek1 == "2":
            user_menu()
        elif secenek1 == "3":
            print("Programdan Çıkılıyor...")
            quit()


def admin_menu():
    while True:
        os.system("clear")
        print()
        print("Yönetici Olarak Giriş Yapıldı.")
        print("-------------------------------------------")
        print("[1]. Ekle")
        print("[2]. Çıkar")
        print("[3]. Göster")
        print("[4]. Ana Menüye Dön")
        print("[5]. Çık")
        print("-------------------------------------------")

        islem = input("Lütfen Bir İşlem Seçin (1/2/3/4/5): ")

        print("-------------------------------------------")


        if islem == "1":
            add_books()
        elif islem == "3":
            show_books()
        elif islem == "4":
            print("Ana Menüye Dönülüyor...")
            return
        elif islem == "5":
            print("Çıkış Yapılıyor...")
            quit()
        elif islem == "2":
            remove_books()
        else:
            print("Yanlış Girdiniz!")

def user_menu():
    while True:
        os.system("clear")
        print()
        print("Kullanıcı Olarak Giriş Yapıldı.")
        print("-------------------------------------------")
        print("[1]. Kitapları Göster")
        print("[2]. Ana Menüye Dön")
        print("[3]. Çık")
        print("-------------------------------------------")

        islem1 = input("Lütfen Bir İşlem Seçin (1/2/3): ")

        print("-------------------------------------------")

        if islem1 == "1":
            show_books()
        elif islem1 == "2":
            print("Ana Menüye Dönülüyor...")
            return
        elif islem1 == "3":
            print("Programdan Çıkılıyor...")
            quit()
        else:
            print("Yanlış Girdiniz!")


def add_books():
    os.system("clear")
    global Kitaplar
    ekleme = input("Eklemek İstediğiniz Kitap: ")
    Kitaplar.append(ekleme)
    print("Kitap Kaydedildi.")


def show_books():
    os.system("clear")
    global Kitaplar
    print("Kitaplar gösteriliyor...")
    print("----------------------------------------")

    for i in Kitaplar:
        print("Kitap Adı --> " + i)

    print("------------------------------------------------")
    print("Ana Menüye Dönmek İçin ENTER Tuşuna Basın")

    cıkıs = ()

    if cıkıs == input():
        return




def remove_books():
    os.system("clear")
    global Kitaplar
    cıkar = input("Çıkarmak İstediğiniz Kitap Adı: ")
    cıkar_lower = cıkar.lower()
    found = False

    for kitap in Kitaplar:
        if kitap.lower() == cıkar_lower:
            Kitaplar.remove(kitap)
            found = True
            print("Kitap Çıkarıldı.")
            break
        
    if not found:
        print("Kitap Bulunamadı")

    print("----------------------------------------------------")
    print("Ana Menüye Dönmek İçin ENTER Tuşuna Basın...")
    cıkıs1 = ()

    if cıkıs1 == input():
        return



main_menu()
