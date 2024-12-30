class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

def knapsack(items, capacity):
    def node_bound_count(i, weight, value):
        if weight > capacity:
            return 0
        node_value = value
        j = i
        total_weight = weight

        while j < len(items) and total_weight + items[j].weight <= capacity:
            node_value += items[j].value
            total_weight += items[j].weight
            j += 1
        if j < len(items):
            node_value += (capacity - total_weight) * (items[j].value / items[j].weight)

        return node_value

    def branch_bound(i, weight, value, nms):
        nonlocal max_value
        nonlocal max_nms
        if weight <= capacity and value > max_value:
            max_value = value
            max_nms = nms
        if i == len(items):
            return 0
        if node_bound_count(i, weight, value) > max_value:
            branch_bound(i + 1, weight, value, nms)
        if value + (capacity - weight) * (items[i].value / items[i].weight) > max_value:
            branch_bound(i + 1, weight + items[i].weight, value + items[i].value, nms + [items[i].name])

    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    max_value = 0
    max_nms = []
    branch_bound(0, 0, 0, [])
    return max_nms, max_value


if __name__ == '__main__':
    items = [Item('r', 3, 25),
             Item('p', 2, 15),
             Item('a', 2, 15),
             Item('m', 2, 20),
             Item('i', 1, 5),
             Item('k', 1, 15),
             Item('x', 3, 20),
             Item('t', 1, 25),
             Item('f', 1, 15),
             Item('d', 1, 10),
             Item('s', 2, 20),
             Item('c', 2, 20)]
    capacity = 8
    max_nms, max_value = knapsack(items, capacity)
    result_nms = []

    for i in range(len(items)):
        if items[i].name in max_nms:
            for j in range(items[i].weight):
                result_nms.append(items[i].name)

    k = 0
    for i in range(len(result_nms)):

        if (k + 1) % 3 == 0 or k + 1 == len(result_nms):
            print([result_nms[i]])

        elif k == 0 or (k + 1) % 3 != 0:
            print([result_nms[i]], end = ', ')

        k += 1
    print(f'Итоговые очки выживания: {max_value}')