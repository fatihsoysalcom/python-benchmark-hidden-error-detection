import time
import sys

def process_data_normal(data):
    """Simulates normal data processing."""
    result = []
    for item in data:
        # Simulate some work
        time.sleep(0.0001)
        result.append(item * 2)
    return result

def process_data_with_bug(data):
    """Simulates data processing with a hidden bug."""
    result = []
    for i, item in enumerate(data):
        # Simulate some work
        time.sleep(0.0001)
        if i % 1000 == 0 and i > 0: # A subtle bug: skips processing for every 1000th item after the first
            continue
        result.append(item * 2)
    return result

def run_benchmark(func, data, iterations=10):
    """Runs a function multiple times and measures its execution time."""
    start_time = time.time()
    for _ in range(iterations):
        func(data)
    end_time = time.time()
    return (end_time - start_time) / iterations

def main():
    # Generate a large dataset to expose potential issues
    dataset_size = 50000
    sample_data = list(range(dataset_size))

    print(f"Running benchmarks with dataset size: {dataset_size}")

    # Benchmark the normal function
    normal_avg_time = run_benchmark(process_data_normal, sample_data)
    print(f"Average time for process_data_normal: {normal_avg_time:.6f} seconds")

    # Benchmark the function with the hidden bug
    buggy_avg_time = run_benchmark(process_data_with_bug, sample_data)
    print(f"Average time for process_data_with_bug: {buggy_avg_time:.6f} seconds")

    # Compare the results
    # A significant difference in execution time can indicate a performance issue or a bug.
    # In this case, the buggy function might appear faster due to skipped operations,
    # but it's incorrect. A more complex bug might cause slowdowns.
    if abs(normal_avg_time - buggy_avg_time) > normal_avg_time * 0.1: # Threshold for significant difference
        print("\nALERT: Significant performance difference detected! This might indicate a hidden bug or inefficiency.")
        # In a real scenario, you'd also verify correctness, not just speed.
        # For this example, the speed difference is the 'signal' for a potential problem.
    else:
        print("\nNo significant performance difference detected.")

    # Example of verifying correctness (optional, but crucial for real bugs)
    print("\nVerifying correctness for a small subset...")
    small_data = list(range(50))
    normal_result = process_data_normal(small_data)
    buggy_result = process_data_with_bug(small_data)

    if normal_result == buggy_result:
        print("Correctness check passed for small subset.")
    else:
        print("Correctness check FAILED for small subset! Bug detected.")
        print(f"Normal result length: {len(normal_result)}")
        print(f"Buggy result length: {len(buggy_result)}")

if __name__ == "__main__":
    main()
