def can_complete_circuit(gas, cost):
    n = len(gas)
    total_gas = 0
    total_cost = 0
    start = 0
    current_gas = 0

    for i in range(n):
        total_gas += gas[i]
        total_cost += cost[i]
        current_gas += gas[i] - cost[i]

        if current_gas < 0:
            start = i + 1
            current_gas = 0

    if total_gas < total_cost:
        return -1

    return start

# Ví dụ sử dụng
gas = [4, 6, 7, 4]
cost = [6, 5, 3, 5]
start = can_complete_circuit(gas, cost)
print(f"start = {start}")