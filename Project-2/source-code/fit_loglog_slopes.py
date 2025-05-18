import pandas as pd
import numpy as np
import argparse
from scipy.stats import linregress


def main():
    parser = argparse.ArgumentParser(description="Fit a line to log-log waste data and estimate slope for each algorithm.")
    parser.add_argument('--input_csv', type=str, required=True, help='CSV file with average waste summary.')
    parser.add_argument('--output_csv', type=str, required=True, help='CSV file to save slopes and intercepts.')
    args = parser.parse_args()

    df = pd.read_csv(args.input_csv)
    results = []
    for alg in sorted(df['algorithm'].unique()):
        sub = df[df['algorithm'] == alg]
        x = np.log(sub['n'])
        y = np.log(sub['average_waste'])
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        results.append({
            'algorithm': alg,
            'slope': slope,
            'intercept': intercept,
            'r_squared': r_value ** 2
        })
        print(f"Algorithm: {alg}, Slope: {slope:.4f}, Intercept: {intercept:.4f}, R^2: {r_value ** 2:.4f}")
    pd.DataFrame(results).to_csv(args.output_csv, index=False)
    print(f"Slope results saved to {args.output_csv}")

if __name__ == "__main__":
    main() 