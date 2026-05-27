import pandas  as pd
import matplotlib.pyplot as plt
import seaborn as sns  # type: ignore

DATASET = "./data/raw/data.csv"

df = pd.read_csv(DATASET)

#Ploting Timeseries
fig, axes = plt.subplots(4,1,figsize=(8,4),sharex=True)
sns.lineplot(data= df, x="time_step",y="temperature", ax=axes[0])
sns.lineplot(data= df, x="time_step",y="vibration", ax=axes[1])
sns.lineplot(data= df, x="time_step",y="pressure", ax=axes[2])
sns.lineplot(data= df, x="time_step",y="health_index", ax=axes[3])
plt.tight_layout()
plt.show()

#Plotting Histogram
plt.figure(figsize=(8,4))
sns.histplot(data=df, x="vibration", kde=True)
plt.show()

# Correlation
plt.figure(figsize=(6,5))
sns.scatterplot(data=df, x="temperature", y="health_index", hue="fault_label")
plt.tight_layout()
plt.show()


plt.figure(figsize=(6,5))
sns.scatterplot(data=df, x="vibration", y="health_index", hue="fault_label")
plt.tight_layout()
plt.savefig("./plots/scatter_vibration_health.png", dpi=150, bbox_inches="tight")
plt.show()
