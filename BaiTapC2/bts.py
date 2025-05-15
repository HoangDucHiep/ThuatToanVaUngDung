class Student:
    def __init__(self, id, name, gender, hometown, student_class, gpa):
        self.id = id
        self.name = name
        self.gender = gender
        self.hometown = hometown
        self.student_class = student_class
        self.gpa = gpa

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Gender: {self.gender}, Hometown: {self.hometown}, Class: {self.student_class}, GPA: {self.gpa}"

class BSTNode:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, student):
        def _insert(root, student):
            if not root: return BSTNode(student)
            if student.id < root.student.id:
                root.left = _insert(root.left, student)
            elif student.id > root.student.id:
                root.right = _insert(root.right, student)
            return root
        self.root = _insert(self.root, student)

    def search(self, id):
        def _search(root, id):
            if not root or root.student.id == id: return root
            if id < root.student.id: return _search(root.left, id)
            return _search(root.right, id)
        result = _search(self.root, id)
        return result.student if result else None

    def delete(self, id):
        def _delete(root, id):
            if not root: return root
            if id < root.student.id:
                root.left = _delete(root.left, id)
            elif id > root.student.id:
                root.right = _delete(root.right, id)
            else:
                if not root.left: return root.right
                if not root.right: return root.left
                min_larger_node = self._find_min(root.right)
                root.student = min_larger_node.student
                root.right = _delete(root.right, min_larger_node.student.id)
            return root
        self.root = _delete(self.root, id)

    def _find_min(self, root):
        while root.left: root = root.left
        return root

    def inorder(self):
        def _inorder(root):
            return _inorder(root.left) + [root.student] + _inorder(root.right) if root else []
        return _inorder(self.root)

# Khởi tạo và sử dụng BST
bst = BinarySearchTree()
bst.insert(Student(1, "Nguyen Van A", "Nam", "Ha Noi", "CTK42", 3.5))
bst.insert(Student(3, "Tran Thi B", "Nu", "Hai Phong", "CTK42", 3.7))
bst.insert(Student(2, "Le Van C", "Nam", "Da Nang", "CTK43", 3.6))

print("Danh sách sinh viên:")
for student in bst.inorder():
    print(student)

print("\nTìm sinh viên ID = 2:")
print(bst.search(2) or "Không tìm thấy")

print("\nXóa sinh viên ID = 3")
bst.delete(3)

print("\nDanh sách sinh viên sau khi xóa:")
for student in bst.inorder():
    print(student)