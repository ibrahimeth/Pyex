# import json

# databa
# se = {"ibrahim" : 91 , "gaye" : 59}

# # x = json.loads(database)
# x = json.dumps(database)
# print(x)
# with open("json_person.txt","w" , encoding="UTF-8") as file :
#     file.write(x)

"""
bakalım denemeler yapalım  öncelikle ben aklımdan yapıcam eğer gerek kalırsa internetten bakıcam.
"""


import json
import os
import time

class User :
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository :
    def __init__(self) -> None:
        self.users = []
        self.isloggedIn = False
        self.currentUser = {}
        self.loadUser()
    def loadUser(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="UTF-8") as file :
                users = json.load(file)
                for user in users :
                    user = json.loads(user)
                    newUser = User(username= user["username"],password= user["password"],email= user["email"])  
                    self.users.append(newUser)
    def Register(self,user : User ) : 
        self.users.append(user)
        self.SavetoFile()
        print("Kullanıcı oluşturuldu.")
        
    def Login(self,username,password):
        for user in self.users :
            if user.username == username and user.password == password :
                self.isloggedIn = True
                self.currentUser = user
                print("GİRİŞ YAPILDI".center(50,"."))
    def SavetoFile(self) :
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open("users.json","w",encoding="UTF-8") as file :
            json.dump(list,file)
        self.loadUser()
    def kapat(self) :
        for i in range(10):
            time.sleep(.3)
            print("." ,end="", flush=True)    
        
        print("ÇIKIŞ yapıldı")
    def control(self):         
        if self.isloggedIn ==  True :
            print("ONLİNE")
        else :
            print("OFFLİNE")
    def çıkışyap(self):
        self.isloggedIn = False
        self.currentUser = {}
        print("Çıkış YAPILDI.")
    def kullanıcılar(self):
        with open("users.json","r",encoding="UTF-8") as file :
            for i in json.load(file) :
                print(i)

repository = UserRepository()

while True :
    print("MENÜ".center(50,"*"))
    sonuc = input("1 - Giriş Yap\n2 - Kayıt Ol\n3 - Kontrol\n4 - Çıkış Yap\n5 - kapat\n6 - KULLANICILAR\n\n==>>")
    if sonuc == "1" :
        username = input("Kullanıcı Adı :")
        password = input("password :")
        repository.Login(username,password)
    if sonuc == "2" :
        username = input("Kullanıcı Adı :")
        password = input("password :")
        email = input("email :")
        user = User(username = username , password= password,email=email)
        repository.Register(user)
        
    if sonuc == "3" :
        repository.control()
    if sonuc == "4" :
        repository.çıkışyap()
    if sonuc== "5":
        repository.kapat()
        break
    if sonuc == "6":
        repository.kullanıcılar()
