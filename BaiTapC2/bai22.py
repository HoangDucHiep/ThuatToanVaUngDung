def merge_products(A, B):
    product_count = {}
    for product in A:
        if product not in product_count:
            product_count[product] = 1
    result = []
    for product in B:
        result.append(product not in product_count)
    return result

A = ["Banana", "Banana", "Apple"]
B = ["Orange", "Apple", "Banana", "Watermelon"]
print(merge_products(A, B))  # [True, False, False, True]