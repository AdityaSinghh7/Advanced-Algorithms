import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import numpy as np


def main():
    parser = argparse.ArgumentParser(description="Plot average waste vs n on a log-log scale for each algorithm, with slope annotation.")
    parser.add_argument('--input_csv', type=str, required=True, help='CSV file with average waste summary.')
    parser.add_argument('--slopes_csv', type=str, required=True, help='CSV file with slopes and intercepts.')
    parser.add_argument('--output_png', type=str, required=True, help='Output PNG file for the plot.')
    args = parser.parse_args()

    df = pd.read_csv(args.input_csv)
    slopes_df = pd.read_csv(args.slopes_csv)
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid", font_scale=1.2)
    for alg in sorted(df['algorithm'].unique()):
        sub = df[df['algorithm'] == alg]
        plt.plot(sub['n'], sub['average_waste'], marker='o', label=alg)
        # Annotate with slope and function
        slope_row = slopes_df[slopes_df['algorithm'] == alg].iloc[0]
        slope = slope_row['slope']
        intercept = slope_row['intercept']
        # Function string: W(A) ≈ C * n^slope
        C = np.exp(intercept)
        func_str = f"W({alg}) ≈ {C:.2f} n^{slope:.2f}"
        # Place annotation near last data point
        x_annot = sub['n'].values[-1]
        y_annot = sub['average_waste'].values[-1]
        plt.annotate(f"slope={slope:.2f}\n{func_str}",
                     xy=(x_annot, y_annot),
                     xytext=(10, 0), textcoords='offset points',
                     fontsize=10, color='black',
                     arrowprops=dict(arrowstyle='->', lw=0.5))
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('n (log scale)')
    plt.ylabel('Average Waste W(A) (log scale)')
    plt.title('Average Waste vs n (log-log scale) for Bin Packing Algorithms')
    plt.legend(title='Algorithm')
    plt.tight_layout()
    plt.savefig(args.output_png)
    print(f"Annotated plot saved to {args.output_png}")

if __name__ == "__main__":
    main() 