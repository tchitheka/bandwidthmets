import pandas as pd
import matplotlib.pyplot as plt

# Path to CSV file
csv_file = "/home/takondwa/Desktop/focus/inethi_FOCUS_OV_2024-04-06_11-00-00.csv"
output_file = "network_load_normalized.png"

# Read CSV (tab-separated, no header)
df = pd.read_csv(csv_file, sep="\t", header=None, names=["timestamp", "frame_len"])

# Convert to numeric
df["timestamp"] = df["timestamp"].astype(float)
df["frame_len"] = df["frame_len"].astype(int)

# Convert to datetime for plotting
df["time"] = pd.to_datetime(df["timestamp"], unit="s")

# Bin into 1-second intervals (Mbps)
df = df.set_index("time")
traffic_mbps = (df["frame_len"].resample("1S").sum() * 8) / 1e6  # Mbps

# Normalize (0 to 1)
traffic_norm = traffic_mbps / traffic_mbps.max()

# Plot
plt.figure(figsize=(12,6))
plt.plot(traffic_norm.index, traffic_norm.values, label="Normalized Network Load", color="blue")

plt.title("Normalized Network Load Over Time (Outbound Traffic)")
plt.xlabel("Time")
plt.ylabel("Normalized Load (0–1)")
plt.ylim(0, 1.05)  # keep y-axis between 0 and 1
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

plt.tight_layout()
plt.savefig(output_file, dpi=300)
plt.show()
