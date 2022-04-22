# Bubble Sort

L = [25,17,9,11,8,2]

# def swap(a,b):
#     temp = a
#     a = b
#     b = temp

j = 1
while j < 6:
    i = 0
    while i < 5:
        if L[i] > L[i+1]:
            temp = L[i]
            L[i] = L[i+1]
            L[i+1] = temp
        else:
            pass
        i += 1
    print(f"Pass {j}",L)
    j = j + 1


