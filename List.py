batch_sizes = ["games", "foods", "tables", "chairs", "class", "rated", "foods"]
batch_sizes.append("python")
print(max(batch_sizes))
print(batch_sizes[4:])
print(sorted(batch_sizes, reverse=True))
batch_sizes = "-".join(batch_sizes)
print(batch_sizes)
print("foods" in batch_sizes)
# Remember; List is ordered, it is mutable and it can store multiple occurrences
