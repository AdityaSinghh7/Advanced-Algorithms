# Project 2: Bin Packing Algorithms Experimental Report - To-Do List

## 1. Preparation
- [x] Ensure all five algorithms are implemented: Next Fit (NF), First Fit (FF), Best Fit (BF), First Fit Decreasing (FFD), Best Fit Decreasing (BFD).
- [x] Verify that each algorithm works with bins of size 1.0 and accepts a list of floating-point items.
- [x] Set up a script to generate random lists of items (floats between 0.0 and 0.35) for various values of n.

## 2. Experimental Setup
- [x] Decide on the range of n: 10, 100, 500, 1000, 2500, 5000, 10,000.
- [x] For each n, generate multiple random sequences (e.g., 20-50 trials per n) to average out randomness.
- [x] For each sequence, run all five algorithms and record:
    - Number of bins used
    - Total size (sum) of all items
    - Waste W(A) = (number of bins used) - (total size of items)

## 3. Data Collection
- [x] Store results for each algorithm, n, and trial in a structured format (e.g., CSV, pandas DataFrame).
- [x] Compute the average waste for each algorithm and each n over all trials.

## 4. Plotting
- [x] For each algorithm, plot average waste W(A) vs n on a log-log scale.
- [x] Fit a line to the log-log plot for each algorithm to estimate the slope.
- [x] Annotate each plot with the estimated slope and the function W(A) as a function of n.

## 5. Analysis
- [x] Compare the slopes and waste functions for all algorithms.
- [x] Identify which algorithm produces the least waste as n grows.
- [x] Prepare a written explanation for why the best algorithm performs better.

## 6. Report Writing
- [ ] Write clear explanations of each algorithm (NF, FF, BF, FFD, BFD).
- [ ] Include all plots and slope estimates in the report.
- [ ] Summarize findings and provide the estimated waste function for each algorithm.
- [ ] Ensure correct English grammar and spelling throughout the report.
- [ ] Conclude with a discussion of the best algorithm and justification.

## 7. Submission
- [ ] Compile the report and plots into a single PDF or document as required.
- [ ] Submit the report electronically to Gradescope. 