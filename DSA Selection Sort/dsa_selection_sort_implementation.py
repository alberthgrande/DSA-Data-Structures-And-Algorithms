my_array = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(my_array)
for i in range(n - 1):
    min_array = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_array]:
            min_array = j
    min_value = my_array.pop(min_array)
    my_array.insert(i, min_value)

print("Sorted array:", my_array)
