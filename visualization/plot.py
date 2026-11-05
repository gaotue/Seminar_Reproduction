import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("data.csv")

# Reshape data from wide format to long format
df_long = df.melt(id_vars=["sequence"], var_name="Step", value_name="Value").dropna()

# Convert Step to numeric for correct x-axis positioning
df_long["Step"] = pd.to_numeric(df_long["Step"])

# Set visual style
sns.set_theme(style="whitegrid")

# Create line plot
plt.figure(figsize=(10, 5))
ax = sns.lineplot(
    data=df_long,
    x="Step",
    y="Value",
    hue="sequence",
    style="sequence",  # Gives each sequence a different dash style/marker
    markers=True,  # Uses distinct markers per line
    dashes=False,  # Set to True if you want dashed lines
    alpha=0.7,  # Transparency makes overlapping lines blend/darken
    linewidth=2.5,
    markersize=8,
)

# Add a horizontal line at y = 96.9
plt.axhline(
    y=96.9,
    color="crimson",
    linestyle="--",
    linewidth=1.8,
    label="Target (96.9)",
)

# Customization
plt.title("Final Results from Repeated Runs", fontsize=14, fontweight="bold")
plt.xlabel("Run", fontsize=12)
plt.ylabel("% CI-SC", fontsize=12)
plt.xticks(range(1, 11))  # Ensure integer ticks 1 to 10
plt.legend(title="sequence", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()
plt.show()