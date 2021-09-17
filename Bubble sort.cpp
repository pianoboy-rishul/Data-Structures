#include<stdio.h>
main()
{
	int arr[10], i, j, n, temp;
	printf("Enter the number of elements to be sorted: ");
	scanf("%d",&n);
	printf("\n\tEntering the list of numbers (as per given order):\n");
	for(i=0;i<n;i++)
	{
		printf("Number-%d : ",i);
		scanf("%d",&arr[i]);
	}
	printf("\n\t...Performing Bubble Sort...\n");					//BUBBLE SORT ALGO//
	for(i=0;i<n-1;i++)
	{
		for(j=0;j<n-i-1;j++)
		{
			if(arr[j]>arr[j+1])
			{
				temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
			}
		}
	}
	printf("\nThe sorted list is as follows:  ");
	for(i=0;i<n;i++)
	{
		printf("%d ",arr[i]);
	}
}
