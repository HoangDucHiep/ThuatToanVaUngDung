import heapq

def multi_phase_merge_sort(input_file, output_file):
    def fibonacci_sequence(n):
        fib = [1, 1]
        while sum(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib

    def distribute_runs(data, fib):
        runs = []
        start = 0
        for length in fib:
            if start >= len(data):
                break
            runs.append(data[start:start + length])
            start += length
        return runs

    def merge_runs(runs):
        while len(runs) > 1:
            next_runs = []
            for i in range(0, len(runs) - 1, 2):
                next_runs.append(list(heapq.merge(runs[i], runs[i + 1])))
            if len(runs) % 2 == 1:
                next_runs.append(runs[-1])
            runs = next_runs
        return runs[0]

    with open(input_file, 'r') as f:
        data = list(map(int, f.read().split()))
    fib = fibonacci_sequence(len(data))
    runs = distribute_runs(sorted(data), fib)
    sorted_data = merge_runs(runs)

    with open(output_file, 'w') as f:
        f.write(' '.join(map(str, sorted_data)))

# Main code to test
if __name__ == "__main__":
    # Sample data
    with open("input.txt", 'w') as f:
        f.write("10 20 5 3 8 12 25 7")

    # Test Multi-phase Merge Sort
    multi_phase_merge_sort("input.txt", "output.txt")
    print("Multi-phase Merge Sort result written to", "output.txt")
