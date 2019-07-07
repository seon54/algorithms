#include <stdio.h>
#include <stdlib.h>
#define TRUE 1
#define FALSE 0

struct Node
{
    int data;
    struct Node *next;
};

struct LinkedList
{
    int numOfItems;
    struct Node *head;
    struct Node *tail;
    struct Node *cur;
};

void ListInit(struct LinkedList *plist)
{
    plist->numOfItems = 0;
    plist->head = NULL;
    plist->tail = NULL;
    plist->cur = NULL;
}

int IsEmpty(struct LinkedList *plist)
{
    if (plist->numOfItems == 0)
        return TRUE;

    else
        return FALSE;
}

int ListItemsCount(struct LinkedList *plist)
{
    return plist->numOfItems;
}

int Find(struct LinkedList *plist, int pdata)
{
    struct Node *temp;
    if (IsEmpty(plist))
        return FALSE;
    else
        temp = plist->head;

    while (1)
    {
        if (temp->next != NULL)
        {
            if (temp->data == pdata)
                return TRUE;
            else
                temp = temp->next;
        }
        else
        {
            if (temp->data == pdata)
                return TRUE;
            else
                return FALSE;
        }
    }
    return FALSE;
}

int RemoveItem(struct LinkedList *plist, int pdata)
{
    struct Node *delNode;
    struct Node *prev;

    if (IsEmpty(plist))
        return FALSE;
    else
    {
        delNode = plist->head;
        prev = plist->head;
    }

    // 첫번째 노드가 pdata일 경우
    if (delNode->data == pdata)
    {
        plist->head = plist->head->next;
        free(delNode);
        (plist->numOfItems)--;
        return TRUE;
    }
    // 두번째 노드 이후가 pdata일 경우
    else
    {
        delNode = delNode->next;
    }

    while (1)
    {
        if (delNode->next != NULL)
        {
            if (delNode->data == pdata)
            {
                prev->next = delNode->next;
                free(delNode);
                (plist->numOfItems)--;
                return TRUE;
            }
            else
            {
                prev = delNode;
                delNode = delNode->next;
            }
        }
        // 마지막 노드
        else
        {
            if (delNode->data == pdata)
            {
                prev->next = NULL;
                plist->tail = prev;
                free(delNode);
                (plist->numOfItems)--;
                return TRUE;
            }
        }
    }
    return FALSE;
}