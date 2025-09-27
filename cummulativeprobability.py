import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------
# 1. Load Argus export
# -------------------
df = pd.read_csv("/kaggle/input/outbound-latency/latency_outboun_results_truncated.csv")

# -------------------
# 2. Extract valid tcprtt values (convert to ms)
# -------------------
tcprtt_ms = df["ack_rtt"].dropna() * 1000
tcprtt_ms = tcprtt_ms[(tcprtt_ms > 0) & (tcprtt_ms <= 1000)]   # ✅ limit max latency

# -------------------
# 3. Build CDF helper
# -------------------
def make_cdf(data):
    sorted_data = np.sort(data)
    cdf = np.arange(1, len(sorted_data)+1) / len(sorted_data)
    return sorted_data, cdf

# -------------------
# 4. Compute percentiles (on truncated data)
# -------------------
percentiles = [50, 90, 95, 99]
cutoffs = np.percentile(tcprtt_ms, percentiles)

# -------------------
# 5. Plot CDF curves per percentile cutoff
# -------------------
plt.figure(figsize=(8,6))

colors = ["green", "orange", "blue", "magenta"]
styles = ["-", "--", ":", "-."]

for p, cutoff, color, style in zip(percentiles, cutoffs, colors, styles):
    truncated = tcprtt_ms[tcprtt_ms <= cutoff]
    x, y = make_cdf(truncated)
    plt.plot(x, y, linestyle=style, color=color, 
             label=f"Min-{p}th pctile span")

plt.xlabel("Milliseconds")
plt.ylabel("Cumulative probability")
plt.title("CDF of TCP RTT (Max capped at 1000ms)")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
