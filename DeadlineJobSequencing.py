##...Rishul Ghosh...##
##...N230...##

def DeadlineJobSequencing(arr, t):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j][2] < arr[j+1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    res = [False]*t
    job = ['-1']*t
    for i in range(len(arr)):
        for j in range(min(t-1, arr[i][1]-1), -1, -1):
            if res[j] is False:
                res[j] = True
                job[j] = arr[i][0]
                break
    print(job)

arr = [['J1', 2, 60],
       ['J2', 1, 100],
       ['J3', 3, 20],
       ['J4', 2, 40],
       ['J5', 1, 20]]
print("____________________________________________________________________________")
print("GIVEN SEQUENCE - [Job, Deadline, Profit] :")
print(arr)
print("____________________________________________________________________________")
print("FOLLOWING IS THE SEQUENCING: ")
DeadlineJobSequencing(arr, 3)
print("____________________________________________________________________________")


