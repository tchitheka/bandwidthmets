import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load RTT data from CSV
df = pd.read_csv("rtt_focus_1-14-apr-2024.csv")

latency = (df['tcp.analysis.ack_rtt'].dropna() * 1000)

latency_clean = latency[(latency > 0) & (latency <= 5000)]

latency_clean = latency_clean.sort_values(ascending=False)



print(latency_clean.describe())
print(latency_clean)