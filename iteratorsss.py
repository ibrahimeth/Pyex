# class sırala :
#     def __init__(self,start,stop):
#         self.start = start
#         self.stop = stop
    
#     def __iter__(self) :
#         return self
    
#     def __next__(self):
#         if self.start >= self.stop :
#             x = self.start
#             self.start += 1 
#             return x
#         else :
#             raise StopIteration

# liste = sırala(15,30)

# myiter = iter(liste)

# while True :
#     try : 
#         element = myiter
#         print(element) 
#     except StopIteration :
#         break 
def x() :
    for i in range(1,20):
        yield i**3

for x in x():
    print(x)

