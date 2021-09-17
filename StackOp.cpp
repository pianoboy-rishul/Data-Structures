#include<stdio.h>
#include<stdlib.h>
#define MAX 100
int stk[MAX];
int top=-1;
void pop();
void display();
void push();
void peek();
int main()
{
    int choice;
    while(1)
    {
        printf("Enter 1 for insertion in stack...\n");
        printf("Enter 2 for deletion in a stack...\n");
        printf("Enter 3 for peek operation in a stack...\n");
        printf("Enter 4 for displaying a stack...\n");
        printf("Enter any other number for exiting the program...\n\n");
        printf("...CHOICE PLEASE... :- ");
        scanf("%d",&choice);
        if(choice==1)
        {
        	push();
		}
        else if(choice==2)
        {
        	pop();
        }
        else if(choice==3)
        {
            peek();
        }
        else if(choice==4)
        {
            display();
        }
        else
            exit(0);
    }
}
void push()
{
	int term;
	if(top==MAX-1)
	{
		printf("...STACK OVERFLOW...\n");
	}
	else
	{
		printf("\nEnter element to insert in stack:- ");
		scanf("%d",&term);
		stk[++top]=term;
	}
	printf("\n");
}
void pop()
{
	if(top==-1)
	{
		printf("...STACK UNDERFLOW...\n");
	}
	else
	{
		printf("Element %d popped.",stk[top]);
		top--;
	}
	printf("\n\n");
}
void peek()
{
	if(top==-1)
	{
		printf("...EMPTY STACK...\n");
	}
	else
	{
		printf("Top Element = %d",stk[top]);
	}
	printf("\n\n");
}
void display()
{
	int i;
	if(top==-1)
	{
		printf("...EMPTY STACK...\n\n");
	}
	else
	{
		printf("Generated Stack = ");
		for(i=0; i<=top; i++)
		{
			printf("%d ",stk[i]);
		}
	}
	printf("\n\n");
}
