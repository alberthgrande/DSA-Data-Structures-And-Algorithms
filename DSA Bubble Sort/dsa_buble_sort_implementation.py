my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(n - 1):
    for j in range(n - i - 1):
        print(f"Comparing: {my_array[j]} and {my_array[j + 1]}")
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
            print(
                f"Swapped: {my_array[j]} with {my_array[j + 1]}"
            )  # Prints after a swap


print("Sorted array: ", my_array)
