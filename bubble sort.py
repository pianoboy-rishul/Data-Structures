arr=[6,3,5,4,2]
for i in range(0,4):
    for j in range(0,5-i-1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)