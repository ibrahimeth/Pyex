import re
 
iddia = "python en iyi arkadaşımdır ve pythonu çok severim"
# x =re.match("python" ,iddia)
y = re.search("python" ,iddia)
print(y)

metin = """Guido Van Rossum Python'ı geliştirmeye 1990 yılında başlamış... Yani
aslında Python için nispeten yeni bir dil denebilir. Ancak Python'un çok uzun
bir geçmişi olmasa da, bu dil öteki dillere kıyasla kolay olması, hızlı olması,
ayrı bir derleyici programa ihtiyaç duymaması ve bunun gibi pek çok nedenden
ötürü çoğu kimsenin gözdesi haline gelmiştir. Ayrıca Google'ın da Python'a özel
bir önem ve değer verdiğini, çok iyi derecede Python bilenlere iş olanağı
sunduğunu da hemen söyleyelim. Mesela bundan kısa bir süre önce Python'ın
yaratıcısı Guido Van Rossum Google'de işe başladı..."""

print(re.findall("Python" , metin))   #['Python', 'Python', 'Python', 'Python', 'Python', 'Python']

liste = ["araba" , "motor" , "oyuncak" , "balkon" , "hayvan" , "ev" , "araba" , "araba","özkan","özcan","özhan"]
for i in liste:
    nesne = re.search("öz[kch]an",i)
    if nesne :
        print(nesne.group())