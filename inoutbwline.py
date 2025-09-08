import pandas as pd
import matplotlib.pyplot as plt

# Load Argus-exported CSV
df = pd.read_csv('bandwidth.csv', sep='\s+')

# Convert time column
df["StartTime"] = pd.to_datetime(df["StartTime"])

# Compute inbound and outbound bandwidth in bits/sec
df['out_bps'] = (df['SrcBytes'] * 8) / df['Dur'].replace(0, 1)  # outbound (sent)
df['in_bps']  = (df['DstBytes'] * 8) / df['Dur'].replace(0, 1)  # inbound (received)

# Set time as index
df.set_index('StartTime', inplace=True)

# Resample per second
out_bandwidth = df['out_bps'].resample('1S').sum()
in_bandwidth  = df['in_bps'].resample('1S').sum()

# Plot inbound vs outbound
plt.figure(figsize=(10, 6))
plt.plot(out_bandwidth.index, out_bandwidth.values/1e6, label='Outbound (Mbps)', color='red')
plt.plot(in_bandwidth.index, in_bandwidth.values/1e6, label='Inbound (Mbps)', color='green')

plt.xlabel('Time')
plt.ylabel('Bandwidth (Mbps)')
plt.title('Inbound vs Outbound Bandwidth Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('inbound_outbound_bandwidth.png')
plt.show()
plt.close()