import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#paste -d, delay.csv rate.csv > network_metrics.csv


# Load merged CSV
df = pd.read_csv("network_metrics.csv", names=["timestamp", "delay_ms", "rate_mbps"])

# Drop missing or NaN values
df = df.dropna()

# Create joint plot (scatter + marginal histograms)
sns.jointplot(
    data=df,
    x="delay_ms",
    y="rate_mbps",
    kind="scatter",
    marginal_kws=dict(bins=40, fill=True)
)

plt.xlabel("Delay (milliseconds)")
plt.ylabel("Rate (Mbps)")
plt.show()