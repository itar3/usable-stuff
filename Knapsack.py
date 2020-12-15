def dp_knapsack_get_max(itemList, capacity):
    assert len(itemList) > 0, "tough luck, no item"
    assert type(capacity) == int
    assert capacity > 0, "did you bring your knapsack?"

    memo = [None] * (len(itemList) + 1)
    for j in range(len(memo)):
        memo[j] = [0] * (capacity + 1)

    i = 1
    for item in itemList:
        for j in range(1, (capacity + 1)):
            if item.weight > j:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = max(memo[i - 1][j], item.value + memo[i - 1][j - item.weight])
        i += 1

    return memo[-1][-1]


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


itemList = []
item = Item(4000, 20)
itemList.append(item)
item = Item(3500, 10)
itemList.append(item)
item = Item(1800, 9)
itemList.append(item)
item = Item(400, 4)
itemList.append(item)
item = Item(1000, 2)
itemList.append(item)
item = Item(200, 1)
itemList.append(item)

print(dp_knapsack_get_max(itemList, 20))
