def main():
    # Read the number of jobs
    n = int(input("Enter the number of Jobs\n"))
    
    jobs = []
    for _ in range(n):
        start_time = int(input("Enter start time: "))
        end_time = int(input("Enter end time: "))
        profit = int(input("Enter profit: "))
        jobs.append((start_time, end_time, profit))
    
    # Sort jobs based on end time
    jobs.sort(key=lambda x: x[1])
    
    # Dynamic programming array to store maximum profit up to each job
    dp = [0] * n
    dp[0] = jobs[0][2]  # Profit of the first job
    
    # Fill the dp array
    for i in range(1, n):
        # Profit if the current job is included
        incl_profit = jobs[i][2]
        # Find the latest job that doesn't conflict with the current job
        l = binary_search(jobs, i)
        if l != -1:
            incl_profit += dp[l]
        # Store the maximum profit by including or excluding the current job
        dp[i] = max(incl_profit, dp[i - 1])
    
    # Total profit Lokesh can earn
    lokesh_earnings = dp[-1]
    
    # Calculate the number of jobs and earnings left for others
    total_profit = sum(job[2] for job in jobs)
    earnings_left = total_profit - lokesh_earnings
    jobs_left = n - count_selected_jobs(jobs, dp)
    
    # Output the result
    print("\nThe number of tasks and earnings available for others")
    print("Task:", jobs_left)
    print("Earnings:", earnings_left)

def binary_search(jobs, index):
    # Binary search to find the latest job that doesn't conflict with jobs[index]
    low, high = 0, index - 1
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid][1] <= jobs[index][0]:
            if mid + 1 <= high and jobs[mid + 1][1] <= jobs[index][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1

def count_selected_jobs(jobs, dp):
    # Count the number of jobs selected by Lokesh
    count = 0
    i = len(dp) - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i - 1]:
            count += 1
            # Find the latest non-conflicting job
            l = binary_search(jobs, i)
            i = l
        else:
            i -= 1
    return count

if __name__ == "__main__":
    main()