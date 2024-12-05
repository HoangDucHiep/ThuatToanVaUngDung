

def vector_beautiful(list):
    """List of numbers"""
    setList = set(list)
    return len(list) - len(setList)


print(vector_beautiful([2, 3, 6, 3]))
print(vector_beautiful([1, 2, 3]))