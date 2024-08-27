prev1 = 0
prev2 = 1

print(prev1)
print(prev2)

count = 2


def F(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        F(prev1, prev2)


F(1, 0)
