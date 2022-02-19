# A tuple is an immutable, ordered sequence of elements, you basically cannot edit the values you have inputted
# A tuple is an immutable, ordered data structure that can be indexed and sliced like a list.
location = (13.4125, 103.866667)
print("Latitude: ", location[0])
print("Longitude: ", location[1])
print(len(location))

dimensions = 52, 40, 100
length, width, height = dimensions  # Tuple unpacking. You can as well just use length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))
print(sorted(dimensions))