import matplotlib.pyplot as plt
import pandas as pd

merged_returns_df = pd.read_csv('./merged_returns.csv', index_col=0)
fig = plt.figure(dpi=400, figsize=(12,5))
merged_returns_df.plot(ax = plt.gca())
plt.ylabel('Cumulative Return')
plt.xlabel('Date')
plt.title('Compare Cumulative Returns')
plt.grid()