import matplotlib.pyplot as plt
dataA= [83,75,90,88]
dataB= [70,83,65,82]
dataC= [82,98,80,94]
sepalate = ['Q1','Q2','Q3','Q4']
plt.plot(sepalate,dataA,marker="o",color="blue")
plt.plot(sepalate,dataB,marker="x",color="orange")
plt.plot(sepalate,dataC,marker="d",color="green")
plt.ylim(50,100)
plt.show()