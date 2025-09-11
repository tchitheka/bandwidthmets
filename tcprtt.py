import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load CSV
df = pd.read_csv("uct_lab_tcp_rtt_analysis.csv")

# Drop rows without RTT
df_rtt = df.dropna(subset=["tcp.analysis.ack_rtt"]).copy()

# Convert epoch to datetime
df_rtt["time"] = pd.to_datetime(df_rtt["frame.time_epoch"], unit="s")

# Convert RTT to milliseconds
df_rtt["rtt_ms"] = df_rtt["tcp.analysis.ack_rtt"] * 1000 

# Plot RTT over time
plt.figure(figsize=(10,5))
plt.plot(df_rtt["time"], df_rtt["rtt_ms"], marker="o", linestyle="-")

plt.xlabel("Time")
plt.ylabel("RTT (ms)")
plt.title("TCP RTT over Time")
plt.grid(True, which='both', axis='both')
plt.grid(True)

# Format x-axis like your example (MM DD:HH:MM)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m %H:%M"))

plt.xticks(rotation=45)  # Rotate labels for readability
plt.tight_layout()
plt.show()
