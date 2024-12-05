class entry:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value
        
    def get_key(self):
        return self.__key
    
    def get_value(self):
        return self.__value
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, entry):
            return self.__key == other.get_key()
        return False

    def __hash__(self) -> int:
        return hash(self.__key)  # Đảm bảo 'entry' có thể dùng trong set
    
class my_map:
    def __init__(self):
        self.__container = set()
        self.__size = 0
        
    def insert(self, key, value):
        for item in self.__container:
            if item.get_key() == key:
                # Nếu khóa tồn tại, cập nhật giá trị mới
                self.__container.remove(item)  # Xóa mục cũ
                updated_item = entry(key, value)  # Tạo mục mới với giá trị được cập nhật
                self.__container.add(updated_item)  # Thêm mục mới
                return
        # Nếu khóa chưa tồn tại, thêm cặp khóa-giá trị mới
        new_item = entry(key, value)
        self.__container.add(new_item)
        self.__size += 1
        
    
