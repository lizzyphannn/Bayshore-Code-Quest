friends = ["Tyna", "Jingyi", "Aggy", "Alice", "Maze"]
lucky_numbers = [1, 3, 10, 22, 28, 19, 29, 30]

friends.extend(lucky_numbers)
print(friends)

friends.append("Wyatt")
print(friends)

friends.insert(3, "Wyatt")
print(friends)

friends.remove("Aggy")
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

print(friends.index("Alice"))

lucky_numbers.reverse()
print(lucky_numbers)

best_friends = friends.copy()
print(best_friends)
