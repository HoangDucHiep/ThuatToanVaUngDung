def sorted_set(arr) -> list:
    return sorted(set(arr)) #even after set(arr), we have the sorted set, but that's not intented, so i sort it again

if __name__ == "__main__":
    print("=== Tets ===")
    print("arr = [apple, banana, apple, apple, banana, orange, appel] \n=> " + sorted_set(["apple", "banana", "apple", "apple", "banana", "orange", "appel"]).__str__())