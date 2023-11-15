import random


hastalik = ["disease","sickness","aliment"]
izin_başlanıç = "permisso start"
tespit = ["detection" , "fixing"]
sincap = "Squirrel"
tatıl_gırsıı = "holiday entrance"
etiket = "ticket"
davul = "drum"
ateş_ölçüsü = "measuring fever"
takas ="swap"
i = 0
while i <= 10 :
    a = random.randint(0,2)
    b = random.randint(0,1)
    # hastalık izni başlangıç tespit sincap giriş tatil etiketi davul ateş ölçüsü takas
    t1 = f"{hastalik[a]} {izin_başlanıç} {tespit[b]} {sincap} \n" 
    t2 = tatıl_gırsıı + " " + etiket + " " + davul + " " + ateş_ölçüsü + " " + takas
    i += 1
    print(t1+t2+"\n")
    print("".center(150,"*"))
