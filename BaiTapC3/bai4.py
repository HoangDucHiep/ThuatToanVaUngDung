import os
import heapq
import shutil


def create_runs(input_file, temp_dir, memory_limit=100):
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    runs = []
    try:
        with open(input_file, 'r') as input_f:
            current_run = []
            for line in input_f:
                try:
                    current_run.append(int(line.strip()))
                except ValueError:
                    # Bỏ qua các dòng không hợp lệ
                    continue

                if len(current_run) >= memory_limit:
                    current_run.sort()
                    run_file = os.path.join(temp_dir, f'run_{len(runs)}.txt')
                    with open(run_file, 'w') as run_f:
                        for item in current_run:
                            run_f.write(f"{item}\n")
                    runs.append(run_file)
                    current_run = []

            # Ghi run cuối cùng nếu còn dữ liệu
            if current_run:
                current_run.sort()
                run_file = os.path.join(temp_dir, f'run_{len(runs)}.txt')
                with open(run_file, 'w') as run_f:
                    for item in current_run:
                        run_f.write(f"{item}\n")
                runs.append(run_file)
    except IOError:
        print(f"Lỗi: Không thể đọc file {input_file}")
    return runs


def merge_two_files(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
            line1 = f1.readline().strip()
            line2 = f2.readline().strip()

            while line1 and line2:
                try:
                    val1 = int(line1)
                    val2 = int(line2)

                    if val1 <= val2:
                        out.write(f"{val1}\n")
                        line1 = f1.readline().strip()
                    else:
                        out.write(f"{val2}\n")
                        line2 = f2.readline().strip()
                except ValueError:
                    line1 = f1.readline().strip() if not line1 else line1
                    line2 = f2.readline().strip() if not line2 else line2

            # Ghi các phần tử còn lại
            while line1:
                try:
                    out.write(f"{int(line1)}\n")
                    line1 = f1.readline().strip()
                except ValueError:
                    line1 = f1.readline().strip()

            while line2:
                try:
                    out.write(f"{int(line2)}\n")
                    line2 = f2.readline().strip()
                except ValueError:
                    line2 = f2.readline().strip()
    except IOError:
        print(f"Lỗi: Không thể ghi hoặc đọc file {output_file}")


def natural_merge_sort(runs, temp_dir, output_file):
    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                merged_file = os.path.join(temp_dir, f'merged_run_{len(new_runs)}.txt')
                merge_two_files(runs[i], runs[i + 1], merged_file)
                new_runs.append(merged_file)
            else:
                new_runs.append(runs[i])  # Giữ lại run cuối cùng nếu số lượng lẻ
        runs = new_runs

    if runs:
        os.rename(runs[0], output_file)


def balanced_multiway_merge(runs, temp_dir, output_file, num_ways=3):
    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), num_ways):
            ways = runs[i:i + num_ways]
            if len(ways) > 1:
                merged_file = os.path.join(temp_dir, f'balanced_merged_run_{len(new_runs)}.txt')
                multiway_merge(ways, merged_file)
                new_runs.append(merged_file)
            else:
                new_runs.extend(ways)
        runs = new_runs

    if runs:
        os.rename(runs[0], output_file)


def multiway_merge(files, output_file):
    try:
        file_handles = [open(f, 'r') for f in files]
        heap = []

        # Nạp phần tử đầu tiên từ mỗi file
        for i, f in enumerate(file_handles):
            line = f.readline().strip()
            if line:
                try:
                    heapq.heappush(heap, (int(line), i))
                except ValueError:
                    continue

        with open(output_file, 'w') as out:
            while heap:
                value, file_index = heapq.heappop(heap)
                out.write(f"{value}\n")

                # Đọc phần tử tiếp theo từ file
                line = file_handles[file_index].readline().strip()
                if line:
                    try:
                        heapq.heappush(heap, (int(line), file_index))
                    except ValueError:
                        continue

        for f in file_handles:
            f.close()
    except IOError:
        print(f"Lỗi: Không thể ghi hoặc đọc file {output_file}")


def multipass_merge_sort(runs, temp_dir, output_file):
    """
    Phương pháp trộn đa pha (Multipass Merge).
    """
    pass_count = 0
    while len(runs) > 1:
        new_runs = []
        pass_count += 1

        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                merged_file = os.path.join(temp_dir, f'multipass_run_{pass_count}_{len(new_runs)}.txt')
                merge_two_files(runs[i], runs[i + 1], merged_file)
                new_runs.append(merged_file)
            else:
                new_runs.append(runs[i])

        runs = new_runs

    if runs:
        os.rename(runs[0], output_file)


# Tạo file dữ liệu mẫu
input_file = 'input.txt'
output_file = 'output.txt'
temp_dir = 'temp_files'

with open(input_file, 'w') as f:
    import random
    numbers = [random.randint(1, 10000) for _ in range(500)]
    for num in numbers:
        f.write(f"{num}\n")

# 1. Tạo các run
runs = create_runs(input_file, temp_dir, memory_limit=50)

# 2. Chạy từng phương pháp sắp xếp ngoài
print("Phương pháp trộn tự nhiên:")
natural_merge_sort(runs, temp_dir, output_file)

print("Phương pháp trộn đa lối cân bằng:")
balanced_multiway_merge(runs, temp_dir, output_file, num_ways=3)

print("Phương pháp trộn đa pha:")
multipass_merge_sort(runs, temp_dir, output_file)
