#include<stdio.h>
#include<stdlib.h>
#define MAX 20
int que[MAX];
int front=-1;
int rear=-1;
void display();
void ins();
void del();
int main()
{
    int choice;
    while(1)
    {
        printf("Enter 1 for insertion in queue...\n");
        printf("Enter 2 for deletion in a queue...\n");
        printf("Enter 3 for displaying a queue...\n\n");
        printf("...CHOICE PLEASE... - ");
        scanf("%d",&choice);
        if(choice==1)
        {
            ins();
        }
        else if(choice==2)
        {
            del();
        }
        else if(choice==3)
        {
            display();
        }
        else
            exit(0);
    }
}
void ins()
{
    int no;
    printf("Enter the number for insertion: ");
    scanf("%d",&no);
    printf("\n\n");
    if(rear==MAX-1)
    {
        printf("...QUEUE OVERFLOW...\n\n");
    }
    else
    {
        if(rear==-1 && front==-1)
        {
            front=0;
            rear=0;
        }
        else
        {
            rear++;
        }
    }
    que[rear]=no;
}
void del()
{
    int val;
    if(front==-1||front>rear)
    {
        printf("...QUEUE UNDERFLOW...\n\n");
    }
    else
    {
        val=que[front];
        printf("Element %d deleted.\n\n",que[front]);
        front++;
    }
}
void display()
{
    int i;
    if(front==-1||front>rear)
        printf("...EMPTY QUEUE, FILL SOMETHING...\n\n");
    else
    {
        for(i=front;i<=rear;i++)
        {
            printf("%d ",que[i]);
        }
    printf("\n\n");
    }
}
