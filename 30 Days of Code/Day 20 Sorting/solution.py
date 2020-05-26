n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swaps = 0  # keeps track of overall swaps that takes place throughout the iteration
for i in range(n):
    swap_per_iteration = 0  # keeps track of swaps that take place per iteration
    for j in range(n - 1):
        # for sorting the elements in ascending order.
        # if descending is required, we replace '<' with '>'
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swap_per_iteration += 1

    # if swaps per iteration is 0, that means the elements are already sorted and we can exit the loop
    if swap_per_iteration == 0:
        break;
    # if swaps per iteration is not 0, that means the list is not sorted yet and we need to move to next
    # iterations and increase the value of overall swaps
    else:
        swaps += swap_per_iteration
print(F"Array is sorted in {swaps} swaps.")
print(F"First Element: {a[0]}")
print(F"Last Element: {a[-1]}")