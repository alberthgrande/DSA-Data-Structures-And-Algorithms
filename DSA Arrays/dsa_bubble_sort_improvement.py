my_array = [7, 3, 9, 12, 11]

n = len(my_array)

for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        print(f"Comparing: {my_array[j]} and {my_array[j + 1]}")
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
            swapped = True
            print(
                f"Swapped: {my_array[j]} with {my_array[j + 1]}"
            )  # Prints after a swap
        if not swapped:
            break

print("Sorted array: ", my_array)
