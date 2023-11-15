import os
import datetime
import json
import random
zaman = datetime.datetime

print(zaman.today())
class User :
    def __init__(self,hesapID,password):
        self.hesapID = hesapID
        self.password = password
        self.hesap = 0
        self.kredi = 2000
        self.hesapno = random.randint(0000,9999)
class UserRepository:
    def __init__(self):
        self.users = []
        self.IsLogin = False
        self.currentUser = {}
        self.hak = 3
        self.loadUser()
    def loadUser(self):
        if os.path.exists("bigdatabanka.json") :
            with open("bigdatabanka.json", "r+",encoding="UTf-8") as file :
                users = json.load(file)
                for user in users :
                    user = json.loads(user)
                    NewUSer = User(hesapID = user["hesapID"],password=user["password"])
                    self.users.append(NewUSer)
                    
    def register(self,user : User) :
        self.users.append(user)
        self.Saveofile()
        print("KULLANICI OLUŞTURULDU".center(10," "))
    def Saveofile(self):
        list = []
        for user in self.users :
            list.append(json.dumps(user.__dict__))
        with open("bigdatabanka.json","w",encoding="UTF-8") as file :
            json.dump(list,file)
        self.loadUser()
    def login(self,hesapID,password):
        for scan in self.users :
            if hesapID == scan.hesapID and password == scan.password :
                self.IsLogin = True
                self.currentUser = scan
                print("GİRİŞ YAPILDI HOŞGELDİNİZ.".center(75,"*"))
                while True :
                    value = input("1 - Para Çek\n2 - Para Yatır\n3 - Bakiye Öğren\n4 - EFT gönder\n5 - KAPAT\n==>>")  
                    if value == "1" :
                        self.paracek(scan)
                        continue
                    if value == "2" :
                        self.parayatır(scan)
                    if value == "3" :
                        self.Bakiyeogren(scan)
                        continue
                    if value == "4" :
                        pass
                    if value == "5" :
                        break
            elif not hesapID == scan.hesapID and password == scan.password :
                print("yanlış")
    def logout(self):
        pass
    def paracek(self,scan):
        tutar = int(input(f"{scan.hesapno} no'lu hesabınızdan Çekmek istediğiniz tutar:"))
        if scan.hesap - tutar >= 0 :
            scan.hesap = scan.hesap - tutar
            self.Bakiyeogren(scan)
        elif scan.hesap - tutar < 0 :
            seçim = input("kredi çekmek istermisiniz ?? faizi %10 dolar olmuş 13 (e/h)")
            if seçim  == "e" :
                if scan.kredi > 0 :
                    print(f"kredi alabileceğiniz tutar {scan.kredi} ")
                    y = int(input("kaç tl kredi istiyorsunuz : "))
                if scan.kredi - y >= 0 :
                    print(f"başarılı")
                    scan.kredi -= y
                    self.Bakiyeogren(scan)
                else :
                    print("kredi limit yetersiz.")
            elif seçim == "h":
                pass
    def parayatır(self,scan):
        tutar = int(input(f"{scan.hesapno} no'lu hesabınıza yatırmak istediğiniz tutar:"))
        if 2000 - scan.kredi > 0 :
            if tutar  >= 2000 - scan.kredi:
               kalan = tutar - (2000 - scan.kredi) 
               scan.hesap += kalan
               self.Bakiyeogren(scan )
            else:
                pass
        else:
               scan.hesap += tutar
               self.Bakiyeogren(scan)
    def Bakiyeogren(self,scan):
        print(f"SAYIN {scan.hesapID}, {scan.hesapno} numaralı hesabınızın kalan bilgisi ".center(100," ")) 
        print(f"HESAP BAKİYESİ :{scan.hesap}".center(100," ")) 
        print(f"KREDİ LİMİTİ :{scan.kredi} , Borç: {2000-scan.kredi}".center(100," "))
    def fileread(self) :
        with open("bigdatabanka.json","r",encoding="UTF-8") as file :
            users = json.load(file)
            for kayıtlı in users :
                kayıtlı = json.loads(kayıtlı)
                print(kayıtlı)


repository = UserRepository()
repository.fileread()

while True:
    print("".center(100,"*"))
    print("MENU".center(100,"*"))
    print("".center(100,"*"))
    print("hoşgeldiniz lütfen işlem seçiniz...".center(100," "))
    result = input("\n"+"1 - giriş yap\n2 - kayıt ol\n3 - KAPAT\n\n==>>" )
    if result == "1" :
        repository.hak -= 1
        if repository.hak > 0 : 
            hesapID = input("hesap adınız :")
            password = input("şifre :")
            repository.login(hesapID=hesapID,password=password)
            if repository.IsLogin == True :
                break
        else :
            print("kartınız BLOKE OLDU. Hesap bilgileri silindi .. Müşteri temsilicisini arayınız.")

    if result == "2":
        hesapID = input("hesap adınız :")
        password = input("şifre :")
        passwordC = input("şifre tekrar :")
        user = User(hesapID=hesapID,password=password)
        repository.register(user)
    if result == "3" :
        break

