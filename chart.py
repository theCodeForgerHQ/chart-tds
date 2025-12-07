import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
sns.set_context("talk")

np.random.seed(42)

channels = ["Email", "Phone", "Live Chat", "Social Media"]
data = []

for channel in channels:
    if channel == "Email":
        times = np.random.normal(loc=8, scale=2, size=200)
    elif channel == "Phone":
        times = np.random.normal(loc=5, scale=1.5, size=200)
    elif channel == "Live Chat":
        times = np.random.normal(loc=3, scale=1, size=200)
    else:
        times = np.random.normal(loc=6, scale=2, size=200)
    times = np.clip(times, a_min=0.5, a_max=None)
    for t in times:
        data.append({"Channel": channel, "ResponseTime": t})

df = pd.DataFrame(data)

plt.figure(figsize=(8, 8))
sns.violinplot(x="Channel", y="ResponseTime", data=df, palette="Set2", inner="quartile")
plt.title("Customer Support Response Time Distribution by Channel")
plt.xlabel("Support Channel")
plt.ylabel("Response Time (hours)")

plt.savefig('src/chart.png', dpi=64)
plt.close()
