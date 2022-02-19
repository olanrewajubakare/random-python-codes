# Sets are data types for mutable unordered collections of unique elements (i.e. unique elements that are without a
# particular ordering
Lanre = ["Bakare", "Victor", "Olanrewaju", "Olanrewaju", "Olalekan", "Olalekan"]
Lanre = set(Lanre)
# Sets are also created with curly brackets {}
Lanre.add("Onimisi")
print(Lanre)
print(sorted(Lanre))
print("Olalekan" in Lanre)
print(len(Lanre))
print(Lanre.pop()) #Removes random element
print(Lanre)