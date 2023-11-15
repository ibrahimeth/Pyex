
# print(dir(datetime))

# # x = datetime.datetime.now()

# # print(x.strftime("%w"))
# now = datetime.datetime.now()
# clock = datetime.datetime.hour
# m = datetime.datetime.isoformat(now)
# y = datetime.datetime.fromisoformat(m)

# print(y)

# class deneyelim() :
#     x=int(input("x : "))
#     y=int(input("y : "))
#     def __init__(self,x,y) :
#         self.x = x
#         self.y = y
#     def toplama(self,x,y):
#         print(x+y)
#     def çıkarma(self,x,y):
#         print(x-y)
#     def çarpma(self,x,y):
#         print(x*y)
#     def bölme(self,x,y):
#         print(x/y)




class game:
    def __init__(self,boy = 190 ,kilo = 91) -> None:
        self.boy = boy
        self.kilo = kilo
    def indeks(self):
        
        print(self.kilo/self.boy**2)


game.indeks()