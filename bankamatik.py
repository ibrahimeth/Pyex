from os import close
from typing import ParamSpecArgs, Tuple
import random

Bigdata = {
    "ibrahimHesap" : {
        "ad" : "ibrahim ethem ",
        "hesapNo" : "123456789",
        "bakiye" : 15000,
        "ekHesap" : 3000,
        "Password" :"555"
    },
    "gayeHesap" : {
        "ad" : "gaye Nur AKBIYIK",
        "hesapNo" : "987654321",
        "bakiye" : 9000,
        "ekHesap" : 2500,
        "Password": "333"
    },
    "admin" : {
        "ad" : "ibrahim ethem akbıyık",
        "hesapNo" : "000000000",
        "bakiye" : 999999999,
        "ekHesap" : 999999999,
        "Password": "3565"
    }
}

def admin(Password):
    if Password == Bigdata["admin"]["Password"]  :
        print(Bigdata)
    else:
        "**********"

def kayıtolma() :
    KHesapad = input("Hesabınızın adı nedir? :")
    Kad = input("adınız ve soyadınız ? :")
    Khesapno = str(random.randint(100000000,999999999))
    Kpassword = input("şifrenizi giriniz .. : ")
        
    Bigdata.update({KHesapad : {
        "ad" : Kad,
        "hesapNo" : Khesapno,
        "bakiye" : 0,
        "ekHesap" : 2000,
        "Password" : Kpassword
    }})

    onay = input(f"Merhaba sayın {Kad} {Khesapno} 'lu hesabınızın adı {KHesapad} ve şifresi {Kpassword} onaylıuor musunuz ? (evet/hayır)..::")
    if onay =="evet" :
        print("Tebrikler Hesap oluşturuldu")
        
    elif onay =="hayır":
        kayıtolma()
    else :
        print(onay)
    
def Parayatır(hesap,miktar):
    sor = input("hangi hesaba para yatımak istersiniz (Ana / EK) : ")
    if sor == "ana" :
        T =  Bigdata[hesap]["bakiye"] + miktar
        Bigdata[hesap]["bakiye"] += miktar
        print(f"Sayın {Bigdata[hesap]['ad']} {Bigdata[hesap]['hesapNo']} lu hesabınızda bakiyeniz {T}")

    elif sor == "ek" :
        T1 =  Bigdata[hesap]["ekHesap"] + miktar
        Bigdata[hesap]["ekHesap"] += miktar
        print(f"Sayın {Bigdata[hesap]['ad']} {Bigdata[hesap]['hesapNo']} lu hesabınızın ek Hesabınız {T1} ")
    else :
        print("doğru kelimeleri giriniz.")

def paraCek(hesap,miktar) :
    if Bigdata[hesap]["bakiye"] >= miktar :
        Bigdata[hesap]["bakiye"] -= miktar
        print(f"işlem başarılı kalan bakiye { Bigdata[hesap]['bakiye'] } TL ")
    else :
        toplam = Bigdata[hesap]["bakiye"] + Bigdata[hesap]["ekHesap"]
        if toplam >= miktar :
            ekHesapKULLANIMI = input("Ek hesabınızı kullanmak istiyor musunuz ? : (EVET/HAYIR) ")
            if ekHesapKULLANIMI== "evet" :
                ekHesapÇekilecek = miktar - Bigdata[hesap]["bakiye"]
                Bigdata[hesap]["bakiye"] = 0
                Bigdata[hesap]["ekHesap"] -= ekHesapÇekilecek
                print(f"işlem başarılı kalan bakiye 0 TL , ekHesap : {Bigdata[hesap]['ekHesap']}TL ")
            else :
                print(f"Sayın {Bigdata[hesap]['ad']} {Bigdata[hesap]['hesapNo']} nolu hesabınızda {Bigdata[hesap]['bakiye']}TL bulunmaktadır")
        else:
            print("üzgünüz yetersiz bakiye.")

def bakiyeogren(hesap) :
    print(f"Sayın {Bigdata[hesap]['ad']} {Bigdata[hesap]['hesapNo']} nolu hesabınızda {Bigdata[hesap]['bakiye']}TL bulunmaktadır ek hesabınızda ise {Bigdata[hesap]['ekHesap']} TL")

acılıskonusması = input("Giriş yapmak için Press 1 , Kayıt olmak için Press 2 :  ")
if acılıskonusması == "1" :
    Hesapad = input("Hesap Adınız nedir :")
    Password = input("Şifre giriniz : ")
elif acılıskonusması == "2" :
    kayıtolma() 
    kayıttext = input("Giriş yapmak için Press 1 , Yeni Kayıt olmak için Press 2 :")
    if kayıttext == "1" :
            Hesapad = input("Hesap Adınız nedir :")
            Password = input("Şifre giriniz : ")
    elif kayıttext =="2" :
        kayıtolma()
    else :
        print(kayıttext = input("Giriş yapmak için Press 1 , Yeni Kayıt olmak için Press 2 :"))

girişhak = 2
dongu = 1
admin(Password)

if Password == Bigdata[Hesapad]["Password"] :
    print(f"Hoşgeldiniz Sayın {Bigdata[Hesapad]['ad']}")

while Password == Bigdata[Hesapad]["Password"] :
    menu = input("HANGİ İŞLEMİ YAPMAKİSTİYORSUNUZ BAKİYE ÖĞRNMEK İÇİN PRESS 1 , PARA ÇEKMEK İÇİN PRESS 2, PARA YATIRMAK İÇİN PRESS 3 , Çıkmak için press 4 : " )
    if menu == "1" :
        bakiyeogren(Hesapad)
    elif menu == "2":
        TUTAR = int(input("çekmek istediğiniz tutar :"))
        paraCek(Hesapad,TUTAR)
    elif menu == "3" :
        Tutar2 =int(input("yatırmak istediğiniz Tutar :"))
        Parayatır(Hesapad,Tutar2)
    elif menu== "4":
        break
    elif menu== "admin" :
        s = input("şifre giriniz..:")
        if s == "3565" :
            print(Bigdata)

while not Password == Bigdata[Hesapad]["Password"] :
    print(f"Yalış şifre , kalan hakkınız {girişhak} ")
    Password = input("Şifre giriniz : ")
    girişhak -= 1
    if Password == Bigdata[Hesapad]["Password"] :
        while Password == Bigdata[Hesapad]["Password"] :
            menu = input("HANGİ İŞLEMİ YAPMAKİSTİYORSUNUZ BAKİYE ÖĞRNMEK İÇİN PRESS 1 , PARA ÇEKMEK İÇİN PRESS 2, PARA YATIRMAK İÇİN PRESS 3 , Çıkmak için press 4 : " )
            if menu == "1" :
                bakiyeogren(Hesapad)
            elif menu == "2":
                TUTAR = int(input("çekmek istediğiniz tutar :"))
                paraCek(Hesapad,TUTAR)
            elif menu == "3" :
                Tutar2 =int(input("yatırmak istediğiniz Tutar :"))
                Parayatır(Hesapad,Tutar2)
            elif menu== "4":
                break
            elif menu== "admin" :
                s = input("şifre giriniz..:")
                if s == "3565" :
                    print(Bigdata)
    if girişhak == 0 :
        break