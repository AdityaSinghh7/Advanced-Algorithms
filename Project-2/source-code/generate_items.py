import os
import random
import argparse
import json


def generate_items(n, low=0.0, high=0.35, seed=None):
    if seed is not None:
        random.seed(seed)
    return [random.uniform(low, high) for _ in range(n)]


def main():
    parser = argparse.ArgumentParser(description="Generate random bin packing items.")
    parser.add_argument('-n', type=int, nargs='+', required=True, help='Number(s) of items to generate (can specify multiple)')
    parser.add_argument('--trials', type=int, default=20, help='Number of random sequences to generate for each n (default: 20)')
    parser.add_argument('--low', type=float, default=0.0, help='Minimum item size (default: 0.0)')
    parser.add_argument('--high', type=float, default=0.35, help='Maximum item size (default: 0.35)')
    parser.add_argument('--seed', type=int, default=None, help='Random seed (optional, will be incremented for each trial)')
    parser.add_argument('--output_dir', type=str, default=None, help='Output directory to save JSON files. If not set, prints to stdout.')
    args = parser.parse_args()

    for n in args.n:
        all_trials = []
        for trial in range(args.trials):
            trial_seed = args.seed + trial if args.seed is not None else None
            items = generate_items(n, args.low, args.high, trial_seed)
            all_trials.append(items)
        if args.output_dir:
            os.makedirs(args.output_dir, exist_ok=True)
            out_path = os.path.join(args.output_dir, f"items_n{n}_trials{args.trials}.json")
            with open(out_path, 'w') as f:
                json.dump(all_trials, f)
        else:
            print(f"n={n}, trials={args.trials}")
            print(json.dumps(all_trials))


if __name__ == "__main__":
    main() 