#include <stdlib.h>
#include <stdio.h>
typedef struct Node
{
    int data;
    struct Node* next;
}Node;

Node* insert(Node *head,int data)
{
    Node *p = (Node*)malloc(sizeof(Node*));
    p->data = data;
    p->next = NULL;
    if(head == NULL)
    {
        head = p;
    }
    else{
        Node *x = head;
        while(x->next != NULL) x = x->next;
        x->next = p;
    }
    return head;
}

void display(Node *head)
{
	Node *start=head;
	while(start)
	{
		printf("%d ",start->data);
		start=start->next;
	}
}
int main()
{
	int T,data;
    scanf("%d",&T);
    Node *head=NULL;
    while(T-->0){
        scanf("%d",&data);
        head=insert(head,data);
    }
  display(head);

}
