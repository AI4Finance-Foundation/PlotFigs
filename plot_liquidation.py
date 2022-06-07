import matplotlib.pyplot as plt
import numpy as np

x = list(range(100, 1301, 100))
y1 = [1169436.75, 1281179.21, 1279640.18, 989478.78, 340900.76, 349452.13, 302789.39, 305151.05, 343508.22, 318731.56, 329135.85, 300993.44, 294413.69]
y2 = [1183558.09, 1281092.59, 1280658.77, 1065107.85, 339859.99, 352791.78, 296596.55, 301542.19, 342052.92, 317495.71, 333255.71, 301320.57, 292937.04]

plt.figure()
plt.plot(x, y1, color='red', linewidth=2, linestyle='--', marker='o')
plt.plot(x, y2, color='green', linewidth=2, linestyle='--', marker='s')


plt.title('', fontsize=20)
plt.xlabel('Episode', fontsize=20)
plt.ylabel('Implementation shortfall', fontsize=20)

plt.legend(labels=['Agent1', 'Agent2'], loc='best')



# set grid
plt.grid()


plt.savefig('liquidatin_performance.pdf')

plt.show()

