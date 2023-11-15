from turtle import color
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,marker="o")

# plt.plot(x,y,"o--r")
plt.axis([0,6,0,20])

plt.title("grafik başlığı")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()


