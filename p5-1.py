import matplotlib.pyplot as plt
data = [83,75,90,88]
sepalate = ['Q1','Q2','Q3','Q4']
plt.plot(sepalate,data,marker="o",color="blue",linestyle="-")
plt.ylim(50,100)
plt.show()