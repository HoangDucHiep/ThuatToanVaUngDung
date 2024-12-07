import tempfile
import os
import heapq


class ExternalSort:
    def __init__(self, run_size=100):
        """
        Khởi tạo sắp xếp ngoài.
        - run_size: Số phần tử tối đa mỗi lần đọc vào bộ nhớ để tạo các run.
        """
        self.run_size = run_size
        self.temp_files = []

    def create_runs(self, input_file):
        """
        Tạo các run từ dữ liệu trong file đầu vào và lưu vào file tạm.
        """
        with open(input_file, 'r') as f:
            while True:
                data = f.readlines(self.run_size)
                if not data:
                    break
                run = sorted(map(int, data))  # Sắp xếp run
                temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
                temp_file.writelines(f"{x}\n" for x in run)
                temp_file.close()
                self.temp_files.append(temp_file.name)

    def merge_runs(self, output_file):
        """
        Trộn các run từ các file tạm và ghi kết quả vào file đầu ra.
        """
        min_heap = []
        files = [open(file, 'r') for file in self.temp_files]

        # Khởi tạo heap với phần tử đầu tiên của mỗi file
        for i, file in enumerate(files):
            line = file.readline()
            if line:
                heapq.heappush(min_heap, (int(line.strip()), i))

        # Trộn
        with open(output_file, 'w') as out_file:
            while min_heap:
                value, file_index = heapq.heappop(min_heap)
                out_file.write(f"{value}\n")
                next_line = files[file_index].readline()
                if next_line:
                    heapq.heappush(min_heap, (int(next_line.strip()), file_index))

        # Đóng và xóa file tạm
        for file in files:
            file.close()
        for temp_file in self.temp_files:
            os.remove(temp_file)
        self.temp_files = []

    def run_merge_sort(self, input_file, output_file):
        """
        Phương pháp trộn Run.
        """
        self.create_runs(input_file)
        self.merge_runs(output_file)

    def natural_merge_sort(self, input_file, output_file):
        """
        Phương pháp trộn tự nhiên.
        """
        def find_natural_runs(file):
            file.seek(0)
            runs = []
            current_run = []
            previous = None
            for line in file:
                num = int(line.strip())
                if previous is not None and num < previous:
                    runs.append(current_run)
                    current_run = []
                current_run.append(num)
                previous = num
            if current_run:
                runs.append(current_run)
            return runs

        with open(input_file, 'r') as f:
            while True:
                runs = find_natural_runs(f)
                if len(runs) == 1:
                    break
                self.temp_files = []
                for run in runs:
                    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
                    temp_file.writelines(f"{x}\n" for x in run)
                    temp_file.close()
                    self.temp_files.append(temp_file.name)
                self.merge_runs(output_file)

    def balanced_multiway_merge(self, input_file, output_file, num_files):
        """
        Phương pháp trộn đa lối cân bằng.
        """
        self.create_runs(input_file)
        while len(self.temp_files) > 1:
            files = [open(file, 'r') for file in self.temp_files]
            new_files = []
            for i in range(0, len(files), num_files):
                run_group = files[i:i + num_files]
                temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
                heap = []
                for index, file in enumerate(run_group):
                    line = file.readline()
                    if line:
                        heapq.heappush(heap, (int(line.strip()), index, file))
                with open(temp_file.name, 'w') as out:
                    while heap:
                        value, _, file = heapq.heappop(heap)
                        out.write(f"{value}\n")
                        next_line = file.readline()
                        if next_line:
                            heapq.heappush(heap, (int(next_line.strip()), _, file))
                new_files.append(temp_file.name)
            for file in files:
                file.close()
            for temp in self.temp_files:
                os.remove(temp)
            self.temp_files = new_files

        os.rename(self.temp_files[0], output_file)
        self.temp_files = []

    def multi_phase_merge(self, input_file, output_file):
        """
        Phương pháp trộn đa pha.
        """
        # Khởi tạo các run và lưu vào file tạm
        self.create_runs(input_file)
        while len(self.temp_files) > 1:
            new_files = []
            while len(self.temp_files) > 1:
                temp1, temp2 = self.temp_files.pop(0), self.temp_files.pop(0)
                temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
                with open(temp1, 'r') as f1, open(temp2, 'r') as f2, open(temp_file.name, 'w') as out:
                    heap = []
                    for file in (f1, f2):
                        line = file.readline()
                        if line:
                            heapq.heappush(heap, (int(line.strip()), file))
                    while heap:
                        value, file = heapq.heappop(heap)
                        out.write(f"{value}\n")
                        next_line = file.readline()
                        if next_line:
                            heapq.heappush(heap, (int(next_line.strip()), file))
                os.remove(temp1)
                os.remove(temp2)
                new_files.append(temp_file.name)
            if self.temp_files:
                new_files.append(self.temp_files.pop(0))
            self.temp_files = new_files

        os.rename(self.temp_files[0], output_file)
        self.temp_files = []
input_file = 'input.txt'
output_file = 'output.txt'

# Tạo file dữ liệu đầu vào
with open(input_file, 'w') as f:
    f.writelines(f"{x}\n" for x in [10, 3, 2, 8, 7, 6, 1, 4, 9, 5])

sorter = ExternalSort(run_size=4)

# 1. Phương pháp trộn Run
sorter.run_merge_sort(input_file, output_file)

# 2. Phương pháp trộn tự nhiên
sorter.natural_merge_sort(input_file, output_file)

# 3. Phương pháp trộn đa lối cân bằng
sorter.balanced_multiway_merge(input_file, output_file, num_files=2)

# 4. Phương pháp trộn đa pha
sorter.multi_phase_merge(input_file, output_file)

# In kết quả
with open(output_file, 'r') as f:
    print("Dữ liệu sau khi sắp xếp:", [int(line.strip()) for line in f.readlines()])
