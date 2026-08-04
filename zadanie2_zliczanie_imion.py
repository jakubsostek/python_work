names = ["Ala", "Bartek", "Ala", "Celina", "Bartek", "Ala"]
counts = {}
for name in names:
    if name in counts:
        counts[name]+= 1
    else:
        counts[name] = 1
print(counts)