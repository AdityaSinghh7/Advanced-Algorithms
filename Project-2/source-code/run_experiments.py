import os
import json
import csv
from first_fit import first_fit, first_fit_decreasing
from best_fit import best_fit, best_fit_decreasing
from next_fit import next_fit

ALGORITHMS = {
    'NF': next_fit,
    'FF': first_fit,
    'BF': best_fit,
    'FFD': first_fit_decreasing,
    'BFD': best_fit_decreasing,
}


def run_algorithm(algorithm, items):
    n = len(items)
    assignment = [0] * n
    free_space = []
    algorithm(items, assignment, free_space)
    num_bins = len(free_space)
    total_size = sum(items)
    waste = num_bins - total_size
    return num_bins, total_size, waste


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Run bin packing experiments on generated data.")
    parser.add_argument('--input_dir', type=str, required=True, help='Directory containing generated item JSON files.')
    parser.add_argument('--output_csv', type=str, required=True, help='CSV file to save results.')
    args = parser.parse_args()

    results = []
    for filename in os.listdir(args.input_dir):
        if filename.endswith('.json') and filename.startswith('items_n'):
            n = int(filename.split('_')[1][1:])
            with open(os.path.join(args.input_dir, filename), 'r') as f:
                all_trials = json.load(f)
            for trial_idx, items in enumerate(all_trials):
                for alg_name, alg_func in ALGORITHMS.items():
                    # Defensive copy to avoid in-place modification
                    items_copy = list(items)
                    num_bins, total_size, waste = run_algorithm(alg_func, items_copy)
                    results.append({
                        'n': n,
                        'trial': trial_idx,
                        'algorithm': alg_name,
                        'num_bins': num_bins,
                        'total_size': total_size,
                        'waste': waste
                    })
    # Write results to CSV
    with open(args.output_csv, 'w', newline='') as csvfile:
        fieldnames = ['n', 'trial', 'algorithm', 'num_bins', 'total_size', 'waste']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

if __name__ == "__main__":
    main() 