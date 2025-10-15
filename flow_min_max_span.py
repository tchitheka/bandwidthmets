

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load extracted RTTs
#df = pd.read_csv("/kaggle/input/flow-rtt-v1")
df = pd.read_csv("/home/takondwa/Desktop/focus/all_rtts.csv", on_bad_lines='skip')

# Group by (file, stream) to get per-flow stats
flow_stats = df.groupby(["file", "stream"])["rtt_ms"].agg(
    min_rtt="min",
    max_rtt="max"
).reset_index()

# Compute span = max - min
flow_stats["span_rtt"] = flow_stats["max_rtt"] - flow_stats["min_rtt"]

# Now we can plot CDFs
def plot_cdf(data, label, style):
    sorted_data = np.sort(data)
    yvals = np.arange(1, len(sorted_data)+1) / len(sorted_data)
    plt.plot(sorted_data, yvals, style, label=label)

plt.figure(figsize=(7,5))
plot_cdf(flow_stats["min_rtt"], "Minimum RTT", "r--")
plot_cdf(flow_stats["max_rtt"], "Maximum RTT", "b:")
plot_cdf(flow_stats["span_rtt"], "RTT Span", "g-")

plt.xlabel("Milliseconds")
plt.ylabel("Cumulative probability")
plt.legend()
plt.grid(True, which="both", linestyle="--", alpha=0.7)
plt.xlim(0, 1000)  # if you want to limit
plt.show()

