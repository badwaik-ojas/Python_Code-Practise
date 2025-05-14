def pair_sum(myList, sum):
    seen = []
    pairs = []
    for i, num in enumerate(myList):
        rem = sum - num
        if rem in seen  and (rem, num) not in pairs and (num, rem) not in pairs:
            pairs.append(f"{rem}+{num}")
        seen.append(num)
    return pairs

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))