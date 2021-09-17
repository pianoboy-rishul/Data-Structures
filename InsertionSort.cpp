#include<stdio.h>
main()
{
	int arr[100], i, j, key, n;
	printf("Enter the number of elements in array: ");
	scanf("%d",&n);
	printf("Enter the %d elements: \n",n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
	for(i=0;i<n;i++)
	{
		key=arr[i];
		j=i-1;
		while(j>=0 && arr[j]>key)
		{
            arr[j+1]=arr[j];
            j=j-1;
        }
    	arr[j+1]=key;
	}
	printf("\nThe Sorted Array Generated is: ");
	for(i=0;i<n;i++)
	{
		printf("%d ",arr[i]);
	}
}
