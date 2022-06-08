import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd



val_erl = pd.read_csv("stock_trading_account_value_erl.csv")['0']
y_erl = val_erl / val_erl[0] - 1

dji = pd.read_csv("stock_trading_account_value_dji.csv")

y_dji = dji['close'] / dji['close'][0] - 1

x = dji['date']

ax = plt.subplot(1,1,1)
ax.plot(x, y_erl, color='red', linewidth=1, linestyle='-', )
ax.plot(x, y_dji, color='green', linewidth=1, linestyle='-', )


plt.title('', fontsize=20)
plt.xlabel('Date', fontsize=20)
plt.ylabel('Return', fontsize=20)

plt.legend(labels=['ElegantRL agent', 'DJIA'], loc='best')

# set grid
plt.grid()

#设置每月定位符
ax.xaxis.set_major_locator(mdates.MonthLocator())  # interval = 1

# # 配置横坐标
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

# #设置每隔多少距离⼀个刻度
# plt.xticks(x[::30])

plt.gcf().autofmt_xdate()  # ⾃动旋转⽇期标记


# plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

plt.savefig('stock_trading_performance.pdf')

plt.show()
