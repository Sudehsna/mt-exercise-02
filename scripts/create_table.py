import pandas as pd
import matplotlib.pyplot as plt
from os.path import dirname, abspath

base_dir = dirname(dirname(abspath(__file__))) 

output = f"{base_dir}/data/logs/epochs_ppl_table.tsv"
# Load TSV file
df = pd.read_csv(output, sep='\t')

# Plot as image
fig, ax = plt.subplots(figsize=(df.shape[1] * 1.2, df.shape[0] * 0.4 + 1))
ax.axis('off')
ax.axis('tight')

plt.title("Epoch Perplexity", loc='left', fontsize=12, weight='bold')

table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 cellLoc='center',
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.4)

plt.tight_layout()
plt.savefig("epoch_table.png", dpi=300)
print("Saved as epoch_table.png")
