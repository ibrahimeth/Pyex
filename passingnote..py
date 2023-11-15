from typing import final


class GecmeNotu :
    def __init__(self,vize,final):
        self.vize = vize
        self.final = final
    def hesapla(self) :
        self.vize = int(input("Vize :"))
        final = 60 - (self.vize*2)/5
        print("Finalden en az {final} puanı almalısınız.")
        
gec = GecmeNotu
gec.hesapla(self)