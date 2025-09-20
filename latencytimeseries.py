import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("yahootcprttseries.csv")

# Convert ltime to datetime
df['ltime'] = pd.to_datetime(df['ltime'])

# Convert RTT to ms
df['tcprtt_ms'] = df['tcprtt'] * 1000

# --- Find stats ---
max_idx = df['tcprtt_ms'].idxmax()
min_idx = df['tcprtt_ms'].idxmin()
avg_rtt = df['tcprtt_ms'].mean()

max_time, max_rtt = df.loc[max_idx, ['ltime', 'tcprtt_ms']]
min_time, min_rtt = df.loc[min_idx, ['ltime', 'tcprtt_ms']]

# --- Plot ---
plt.figure(figsize=(12,6))
plt.plot(df['ltime'], df['tcprtt_ms'], color='green', label="RTT samples")

# Add markers
plt.scatter(max_time, max_rtt, color='red', s=100, marker='x', label=f"Max RTT: {max_rtt:.1f} ms")
plt.scatter(min_time, min_rtt, color='blue', s=100, marker='o', label=f"Min RTT: {min_rtt:.1f} ms")
plt.axhline(avg_rtt, color='orange', linestyle='--', label=f"Avg RTT: {avg_rtt:.1f} ms")

# Labels and styling
plt.xlabel("Test duration (days/months)")
plt.ylabel("RTT (ms)")
plt.title("RTT samples over testing period")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
