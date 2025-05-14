lin1 = ["[]","[]","[]"]
lin2 = ["[]","[]","[]"]
lin3 = ["[]","[]","[]"]

map = [lin1, lin2, lin3]
position = input("Provide position to hide your treasure\n")

lin = ["A", "B", "C"]

pos1 = int(position[1])-1
pos2 = lin.index(position[0])
print("POS1",pos1)
print("POS2",pos2)

map[pos1][pos2] = "X"

print(f"{lin1}\n{lin2}\n{lin3}")




