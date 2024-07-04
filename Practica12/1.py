import matplotlib.pyplot as plt

plt.clf()

plt.subplot(221)
plt.plot([4,8,13,17,20],[54,67,98,78,45])

plt.subplot(222)
plt.plot([4,8,13,17,20],[54,67,98,78,45], 'g--o')

x=[4,8,13,17,20],
y=[54,67,98,78,45],
plt.subplot(223)
plt.scatter(x,y)

z= [1,2,3,3,3,2,3,3,3]
num_bins= 8
plt.subplot(224)
n, bins, patches= plt.hist(z, num_bins, facecolor='green')

plt.show()
plt.draw()