import csv
import os
from collections import defaultdict
from os.path import dirname, abspath

base_dir = dirname(dirname(abspath(__file__))) 

output = f"{base_dir}/data/logs/epochs_ppl_table.tsv"
log_dir = f"{base_dir}/data/logs"

# Structure: epoch -> {dropout: ppl}
combined = defaultdict(dict)

# Loop through all log files
for filename in os.listdir(log_dir):
    if filename.startswith("epoch-") and filename.endswith(".tsv"):
        dropout = filename.replace("epoch-", "").replace(".tsv", "")
        with open(os.path.join(log_dir, filename)) as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                epoch = int(row["epoch"])
                ppl = float(row["ppl"])
                combined[epoch][dropout] = ppl

# Get sorted list of all dropout values
all_dropouts = sorted({d for row in combined.values() for d in row})

# Write combined table
with open(output, 'w') as out:
    writer = csv.writer(out, delimiter='\t')
    header = ["Epoch"] + [f"Dropout {d}" for d in all_dropouts]
    writer.writerow(header)

    for epoch in sorted(combined.keys()):
        row = [epoch]
        for d in all_dropouts:
            row.append(f"{combined[epoch].get(d, ''):.2f}")
        writer.writerow(row)

print(f"Table saved to {output}")
