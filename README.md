# Maximum Earnings: Weighted Job Scheduling

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Algorithm](https://img.shields.io/badge/Algorithm-Dynamic%20Programming-blueviolet)

My solution to the HighPeak coding assignment. It's a job-scheduling problem, solved with dynamic programming and binary search in **O(n log n)** time.

## Problem statement

There is a list of jobs, each with a **start time**, **end time**, and **profit**. Lokesh picks first. He can only work on one job at a time, so he chooses the set of non-overlapping jobs that earns him the most. The remaining jobs go to the other employees.

**Goal:** output the number of jobs left, and the total earnings left, for the other employees.

## Approach

This is the classic **weighted job scheduling** problem.

1. **Sort** all jobs by end time.
2. **Dynamic programming.** `dp[i]` holds the maximum profit that can be earned from the first `i + 1` jobs. For each job there are two choices:
   - **Take it:** its profit plus `dp[j]`, where `j` is the latest job that finishes before this one starts
   - **Skip it:** `dp[i - 1]`

   `dp[i] = max(take, skip)`
3. **Binary search.** Because jobs are sorted by end time, the latest compatible job `j` is found in O(log n) instead of O(n).
4. **Backtrack** through `dp` to count how many jobs Lokesh selected.
5. **Result:**
   - Jobs left = total jobs − jobs selected by Lokesh
   - Earnings left = total profit of all jobs − Lokesh's maximum profit

### Complexity

| | |
|---|---|
| Time | O(n log n): sorting, plus a binary search for each job |
| Space | O(n): the DP array |

## How to run

Requires Python 3. There are no external dependencies.

```bash
git clone https://github.com/tanvimvartak/highpeak_Code_Assignment.git
cd highpeak_Code_Assignment
python Max_Earnings.py
```

Enter the number of jobs, then the start time, end time, and profit for each one.

### Example

```
Enter the number of Jobs
3
Enter start time: 900
Enter end time: 1030
Enter profit: 100
Enter start time: 1000
Enter end time: 1200
Enter profit: 500
Enter start time: 1100
Enter end time: 1200
Enter profit: 300

The number of tasks and earnings available for others
Task: 2
Earnings: 400
```

Lokesh takes the second job (profit 500), since it earns more than the other two combined (100 + 300). That leaves 2 jobs worth 400 for the others.

## Repository contents

| File | Description |
|---|---|
| [`Max_Earnings.py`](Max_Earnings.py) | Solution source code |
| [Demo video](Max_Earnings.py%20-%20Visual%20Studio%20Code%202025-02-21%2015-59-45.mp4) | Screen recording of the program running |

## Author

**Tanvi Vartak** · [GitHub](https://github.com/tanvimvartak)
