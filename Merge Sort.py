##...RISHUL GHOSH...##
##...N230...##
##...MERGE SORT...##

def merge(numbers, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = numbers[p + i]
    for j in range(0, n2):
        R[j] = numbers[q + 1 + j]
    i = 0
    j = 0     
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            numbers[k] = L[i]
            i += 1
        else:
            numbers[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        numbers[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        numbers[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(numbers, p, r):
    if p < r:
        q = p+(r-p)//2
        mergeSort(numbers, p, q)
        mergeSort(numbers, q+1, r)
        merge(numbers, p, q, r)

numbers = []
n = int(input("Enter the number of elements in array: "))
print("Enter the elements: ")
for i in range(n):
    ele=int(input())
    numbers.append(ele)
print("***********************************************")
print("Given array is")
for i in range(n):
    print("%d" % numbers[i]),
 
mergeSort(numbers, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % numbers[i])
print("***********************************************")
