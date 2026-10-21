numbers = list(map(int, input("Enter numbers: ").split()))
unique_numbers = sorted(set(numbers))
 
if len(unique_numbers) >= 2:
    print("Second largest:", unique_numbers[-2])
else:
    print("Second largest element does not exist")
