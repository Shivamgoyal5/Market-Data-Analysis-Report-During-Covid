import matplotlib.pyplot as plt  

y=['Low Income','Lower Middle Income','Upper Middle Income','High Income']
x=[4,5,3,1]


plt.bar(y,x)
plt.title('Analysis')
plt.xlabel('Income Rate',fontweight='bold')
plt.ylabel('Frequency',fontweight='bold')
plt.grid(axis='y')
plt.show() 