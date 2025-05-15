def run_sort(input_file, output_file):
    def distribute_runs(input_list, run_size):
        runs = []
        for i in range(0, len(input_list), run_size):
            runs.append(input_list[i:i + run_size])
        return runs

    def merge_runs(run1, run2):
        result = []
        i = j = 0
        while i < len(run1) and j < len(run2):
            if run1[i] < run2[j]:
                result.append(run1[i])
                i += 1
            else:
                result.append(run2[j])
                j += 1
        result.extend(run1[i:])
        result.extend(run2[j:])
        return result

    with open(input_file, 'r') as f:
        data = list(map(int, f.read().split()))

    run_size = 1
    while run_size < len(data):
        runs = distribute_runs(data, run_size)
        data = []
        for i in range(0, len(runs) - 1, 2):
            data.extend(merge_runs(runs[i], runs[i + 1]))
        if len(runs) % 2 == 1:  # Nếu còn Run lẻ, thêm vào cuối
            data.extend(runs[-1])
        run_size *= 2

    with open(output_file, 'w') as f:
        f.write(' '.join(map(str, data)))



# 2. Natural Merge Sort
def natural_merge_sort(input_file, output_file):
    def split_into_runs(data):
        runs = []
        run = [data[0]]
        for i in range(1, len(data)):
            if data[i] < data[i - 1]:
                runs.append(run)
                run = []
            run.append(data[i])
        runs.append(run)
        return runs

    def merge_runs(runs):
        while len(runs) > 1:
            merged_runs = []
            for i in range(0, len(runs), 2):
                if i + 1 < len(runs):
                    merged_runs.append(merge(runs[i], runs[i + 1]))
                else:
                    merged_runs.append(runs[i])
            runs = merged_runs
        return runs[0]

    def merge(run1, run2):
        i, j = 0, 0
        result = []
        while i < len(run1) and j < len(run2):
            if run1[i] < run2[j]:
                result.append(run1[i])
                i += 1
            else:
                result.append(run2[j])
                j += 1
        result.extend(run1[i:])
        result.extend(run2[j:])
        return result

    with open(input_file, 'r') as f:
        data = list(map(int, f.read().split()))

    runs = split_into_runs(data)
    sorted_data = merge_runs(runs)

    with open(output_file, 'w') as f:
        f.write(' '.join(map(str, sorted_data)))


def balanced_multiway_merge(input_file, output_file, num_ways):
    import heapq

    def distribute_runs(data, num_ways):
        runs = [[] for _ in range(num_ways)]
        for i, val in enumerate(data):
            runs[i % num_ways].append(val)
        return runs

    def merge_runs(input_runs, num_ways):
        while len(input_runs) > 1:
            next_runs = []
            for i in range(0, len(input_runs), num_ways):
                merged = list(heapq.merge(*input_runs[i:i + num_ways]))
                next_runs.append(merged)
            input_runs = next_runs
        return input_runs[0]

    with open(input_file, 'r') as f:
        data = list(map(int, f.read().split()))

    runs = distribute_runs(sorted(data), num_ways)
    sorted_data = merge_runs(runs, num_ways)
    with open(output_file, 'w') as f:
        f.write(' '.join(map(str, sorted_data)))



def multi_phase_merge_sort(input_file, output_file):
    import heapq

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



# Test cases
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    # Sample data
    with open(input_file, 'w') as f:
        f.write("10 20 5 3 8 12 25 7")

    # Test Run Sort
    run_sort(input_file, "output1.txt")
    print("Run Sort result written to", output_file)

    # Test Natural Merge Sort
    natural_merge_sort(input_file, "output2.txt")
    print("Natural Merge Sort result written to", output_file)

    # Test Balanced Multiway Merge Sort
    balanced_multiway_merge(input_file, "output33.txt", 3)
    print("Balanced Multiway Merge Sort result written to", output_file)

    # Test Multi-phase Merge Sort
    multi_phase_merge_sort(input_file, "output44.txt")
    print("Multi-phase Merge Sort result written to", output_file)
