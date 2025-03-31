import pandas as pd
import matplotlib.pyplot as plt
from os.path import dirname, abspath

# Set base path and inputs
base_dir = dirname(dirname(abspath(__file__)))

input_epoch = f"{base_dir}/data/logs/epochs_ppl_table.tsv"
input_valid = f"{base_dir}/data/logs/valid_ppl_table.tsv"
chart_epoch = f"{base_dir}/tables_charts/line_chart_epochs.png"
chart_valid = f"{base_dir}/tables_charts/line_chart_valid.png"

def plot_ppl_chart(input_file, output_file, title):
    df = pd.read_csv(input_file, sep="\t")

    plt.figure(figsize=(10, 6))
    x = df.iloc[:, 0]  # Epoch column

    for col in df.columns[1:]:
        plt.plot(x, df[col], label=col)

    plt.title(title)
    plt.xlabel("Epoch")
    plt.ylabel("Perplexity")
    plt.legend(title="Dropout")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    print(f"Saved: {output_file}")

# Plot both
plot_ppl_chart(input_epoch, chart_epoch, "Training Perplexity")
plot_ppl_chart(input_valid, chart_valid, "Validation Perplexity")
