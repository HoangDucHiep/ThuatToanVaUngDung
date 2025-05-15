def count_prefix(contacts, names):
    result = []
    for name in names:
        count = sum(1 for contact in contacts if contact.startswith(name))
        result.append(count)
    return result

contacts = ["Codelearn", "Codewar", "CodePen", "iodie"]
names = ["Code", "Codel", "io"]
print(count_prefix(contacts, names))