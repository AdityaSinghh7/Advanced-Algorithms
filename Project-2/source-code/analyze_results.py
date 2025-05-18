import pandas as pd
import argparse


def main():
    parser = argparse.ArgumentParser(description="Analyze bin packing experiment results.")
    parser.add_argument('--input_csv', type=str, required=True, help='CSV file with experiment results.')
    parser.add_argument('--output_csv', type=str, required=True, help='CSV file to save average waste summary.')
    args = parser.parse_args()

    df = pd.read_csv(args.input_csv)
    # Compute average waste for each algorithm and each n
    summary = df.groupby(['algorithm', 'n'])['waste'].mean().reset_index()
    summary = summary.rename(columns={'waste': 'average_waste'})
    summary.to_csv(args.output_csv, index=False)
    print(f"Averaged results saved to {args.output_csv}")

if __name__ == "__main__":
    main() 