# Bin Packing Algorithms: Experimental Analysis

## 1. Comparison of Slopes and Waste Functions

Based on the log-log plots of average waste versus n for each algorithm, the experimentally determined waste functions and slopes are as follows:

| Algorithm | Slope | Waste Function                |
|-----------|-------|-------------------------------|
| NF        | 0.90  | $W(\text{NF}) \approx 0.05 n^{0.90}$             |
| FF        | 0.42  | $W(\text{FF}) \approx 0.13 n^{0.42}$             |
| BF        | 0.39  | $W(\text{BF}) \approx 0.14 n^{0.39}$             |
| FFD       | 0.05  | $W(\text{FFD}) \approx 0.41 n^{0.05}$            |
| BFD       | 0.05  | $W(\text{BFD}) \approx 0.41 n^{0.05}$            |

- **Slope** indicates how quickly the waste grows as $n$ increases. Lower is better.
- **Waste function** gives the experimental relationship between $n$ and the average waste.

## 2. Best Algorithm as $n$ Grows

- **FFD (First Fit Decreasing)** and **BFD (Best Fit Decreasing)** have the lowest slopes (≈ 0.05), meaning their waste grows extremely slowly with $n$.
- **NF (Next Fit)** has the highest slope (≈ 0.90), so its waste increases rapidly as $n$ increases.
- **FF** and **BF** are intermediate, with moderate slopes (≈ 0.39–0.42).

**Conclusion:**
- **FFD** and **BFD** are the best algorithms for minimizing waste, especially for large $n$.

## 3. Why Do FFD and BFD Perform Best?

FFD and BFD both sort the items in decreasing order before packing. This allows them to place the largest items first, filling bins more efficiently and reducing the chance of leaving large gaps that cannot be filled by smaller items later. As a result, bins are packed more tightly, and the overall waste is minimized.

The experimental results confirm this: both FFD and BFD have a very low slope (≈ 0.05), indicating that the waste grows almost negligibly as the number of items increases. In contrast, algorithms that do not sort the items (NF, FF, BF) leave more waste, especially as $n$ increases.

## 4. Summary Table

| Algorithm | Slope | Waste Function                | Performance as $n$ Grows      |
|-----------|-------|-------------------------------|-------------------------------|
| NF        | 0.90  | $0.05 n^{0.90}$               | Poor (waste grows quickly)    |
| FF        | 0.42  | $0.13 n^{0.42}$               | Moderate                      |
| BF        | 0.39  | $0.14 n^{0.39}$               | Moderate                      |
| FFD       | 0.05  | $0.41 n^{0.05}$               | Excellent (almost constant)   |
| BFD       | 0.05  | $0.41 n^{0.05}$               | Excellent (almost constant)   |

## 5. Recommendation

For practical applications where minimizing waste is critical, **FFD** or **BFD** should be used, as they consistently produce the least waste as the problem size grows. 