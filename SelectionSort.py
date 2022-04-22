# Selection Sort

L = [25,17,9,11,8,2]

j = 0
while j < 5:
    i = j
    while i < 5:
        if L[j] > L[i+1]:
            Smallest_Element = L[j]
            L[j] = L[i+1]
            L[i+1] = Smallest_Element
        else:
            pass
        i += 1
    print(f"Pass {j+1}",L)
    j = j + 1


