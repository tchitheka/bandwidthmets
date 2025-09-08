import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

df = pd.read_csv('bandwidth.csv', sep='\s+')

#print(df)
df["StartTime"] = pd.to_datetime(df["StartTime"])  # Removed unit='s'

df['bps'] = (df['TotBytes'] * 8) / (df['Dur'].replace(0, 1))

df.set_index('StartTime', inplace=True)
bandwidth = df['bps'].resample('1S').sum()

# Plot
plt.figure(figsize=(10, 6))
plt.plot(bandwidth.index, bandwidth.values, label='Bandwidth (Mbps)', color='blue')
plt.xlabel('Time')
plt.ylabel('Bandwidth (Mbps)')
plt.title('Bandwidth Over Time')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('bandwidth_plot.png')
plt.close()
# Save the plot