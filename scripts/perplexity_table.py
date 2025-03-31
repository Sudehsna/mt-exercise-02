import csv
import os
from collections import defaultdict
from os.path import dirname, abspath

base_dir = dirname(dirname(abspath(__file__))) 

output_epoch = f"{base_dir}/data/logs/epochs_ppl_table.tsv"
output_valid = f"{base_dir}/data/logs/valid_ppl_table.tsv"
output_test = f"{base_dir}/data/logs/test_ppl_table.tsv"
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
with open(output_epoch, 'w') as out:
    writer = csv.writer(out, delimiter='\t')
    header = ["Epoch"] + [f"Dropout {d}" for d in all_dropouts]
    writer.writerow(header)

    for epoch in sorted(combined.keys()):
        row = [epoch]
        for d in all_dropouts:
            row.append(f"{combined[epoch].get(d, ''):.2f}")
        writer.writerow(row)

print(f"Epoch_table saved to {output_epoch}")


# Same for Valid Tables

combined = defaultdict(dict)

# Loop through all log files
for filename in os.listdir(log_dir):
    if filename.startswith("valid-") and filename.endswith(".tsv"):
        dropout = filename.replace("valid-", "").replace(".tsv", "")
        with open(os.path.join(log_dir, filename)) as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                epoch = int(row["epoch"])
                ppl = float(row["ppl"])
                combined[epoch][dropout] = ppl

# Get sorted list of all dropout values
all_dropouts = sorted({d for row in combined.values() for d in row})

# Write combined table
with open(output_valid, 'w') as out:
    writer = csv.writer(out, delimiter='\t')
    header = ["Epoch"] + [f"Dropout {d}" for d in all_dropouts]
    writer.writerow(header)

    for epoch in sorted(combined.keys()):
        row = [epoch]
        for d in all_dropouts:
            row.append(f"{combined[epoch].get(d, ''):.2f}")
        writer.writerow(row)

print(f"Epoch_table saved to {output_valid}")



# Structure: model_idx -> {dropout: ppl}
combined = defaultdict(dict)
dropouts = []

# Loop through test files
for filename in os.listdir(log_dir):
    if filename.startswith("test-") and filename.endswith(".tsv"):
        dropout = filename.replace("test-", "").replace("-ppl.tsv", "")
        dropouts.append(dropout)
        with open(os.path.join(log_dir, filename)) as f:
            reader = csv.DictReader(f, delimiter='\t')
            for model_idx, row in enumerate(reader):
                ppl = float(row["ppl"])
                combined[model_idx][dropout] = ppl

dropouts = sorted(set(dropouts), key=float)
models = sorted(combined.keys())

# Write table
with open(output_test, 'w') as out:
    writer = csv.writer(out, delimiter='\t')
    header = ["Model"] + [f"Dropout {d}" for d in dropouts]
    writer.writerow(header)

    for model in models:
        row = [model]
        for d in dropouts:
            val = combined[model].get(d, "")
            row.append(f"{val:.2f}" if val else "")
        writer.writerow(row)

print(f"Test Table saved: {output_test}")
