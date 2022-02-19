manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
items = []
weight = 0
for cargo_name, cargo_weight in manifest:
    print("current weight {}".format(weight))
    if weight >= 100:
        print("breaking loop now!")
        break
    elif weight + cargo_weight > 100:
        print("skipping {} {}".format(cargo_name, cargo_weight))
        continue
    else:
        print("adding {} ({})" .format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight
print("total weight is {}".format(weight))
print("total items added {}".format(items))
