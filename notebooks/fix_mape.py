import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../tables/stability/40.csv')
ax = data.plot(y='MAPE', x='samples')
ax.set_title('Metric stability on MAPE scale', fontweight='bold')
ax.set_ylabel('Expected MAPE')
ax.set_xlabel('Samples')
plt.subplots_adjust(left=0.15)
plt.show()