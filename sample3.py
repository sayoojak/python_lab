marks = {"Anu": 85, "Binu": 70, "Ciya": 95, "David": 80}
 
by_keys = dict(sorted(marks.items()))
by_values = dict(sorted(marks.items(), key=lambda item: item[1]))
 
print("Sorted by keys:", by_keys)
print("Sorted by values:", by_values)
