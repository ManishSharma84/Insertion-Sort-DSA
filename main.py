def insertion_sort(A):
    for i in range(1, len(A)):
        j=i
        while j > 0 and A[j-1] > A[j]:
            A[j], A[j-1] = A[j-1], A[j]
            j -= 1

A = [3, 6, 1,9, 2]
insertion_sort(A)
print(A)
