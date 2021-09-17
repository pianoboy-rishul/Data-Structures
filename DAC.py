##...RISHUL GHOSH...##
##...N230...##
##...70471119030...##
##...Program for Divide and Conquer and finding Max/Min from array...##

print("______________________________________________________________")
print("______________________________________________________________")
def DAC_Max(a, index, l):
    max = -1;
 
    if (index >= l - 2):
        if (a[index] > a[index + 1]):
            return a[index];
        else:
            return a[index + 1];
    max = DAC_Max(a, index + 1, l);
    if (a[index] > max):
        return a[index];
    else:
        return max;

def DAC_Min(a, index, l):
    min = 0;
    if (index >= l - 2):
        if (a[index] < a[index + 1]):
            return a[index];
        else:
            return a[index + 1];
    min = DAC_Min(a, index + 1, l);
    if (a[index] < min):
        return a[index];
    else:
        return min;

if __name__ == '__main__':
    n=int(input("Enter the number of elements in array: "))
    print("______________________________________________________________")
    a=[]
    for i in range(n):
        print("Enter element",i+1,": ")
        ele=int(input())
        a.append(ele)
    print("______________________________________________________________")
    print("Given array: ",a)
    max = DAC_Max(a, 0, n);
    min = DAC_Min(a, 0, n);
    print("The minimum number is : ", min);
    print("The maximum number is : ", max);
    print("______________________________________________________________")
    print("______________________________________________________________")
    


    


      
