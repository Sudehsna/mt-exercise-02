import pandas as pd
import matplotlib.pyplot as plt
from os.path import dirname, abspath

base_dir = dirname(dirname(abspath(__file__))) 

#Create Table for Epoch PPLs
output_epoch = f"{base_dir}/data/logs/epochs_ppl_table.tsv"
# Load TSV file
df = pd.read_csv(output_epoch, sep='\t')

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

# Create Table for Valid PPLs
output_valid = f"{base_dir}/data/logs/valid_ppl_table.tsv"
# Load TSV file
df = pd.read_csv(output_valid, sep='\t')

# Plot as image
fig, ax = plt.subplots(figsize=(df.shape[1] * 1.2, df.shape[0] * 0.4 + 1))
ax.axis('off')
ax.axis('tight')

plt.title("Valid Perplexity", loc='left', fontsize=12, weight='bold')

table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 cellLoc='center',
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.4)

plt.tight_layout()
plt.savefig("valid_table.png", dpi=300)
print("Saved as valid_table.png")

#Create Tables for Test PPLs
output_test = f"{base_dir}/data/logs/test_ppl_table.tsv"
# Load TSV file
df = pd.read_csv(output_test, sep='\t')

# Plot as image
fig, ax = plt.subplots(figsize=(df.shape[1] * 1.2, df.shape[0] * 0.4 + 1))
ax.axis('off')
ax.axis('tight')

plt.title("Test Perplexity", loc='left', fontsize=12, weight='bold')

table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 cellLoc='center',
                 loc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.4)

plt.tight_layout()
plt.savefig("test_table.png", dpi=300)
print("Saved as test_table.png")
