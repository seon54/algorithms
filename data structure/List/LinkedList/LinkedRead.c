#include <stdio.h>
#include <stdlib.h>

typedef struct _node
{
    int data;           // 데이터 담을 공간
    struct _node *next; // Node형 구조체 변수의 주소값을 저장하는 포인터 변수
} Node;

int main(void)
{
    Node *head = NULL; // 리스트의 머리를 가리키는 포인터 변수
    Node *tail = NULL; // 리스트의 꼬리를 가리키는 포인터 변수
    Node *cur = NULL;  // 저장된 데이터의 조회에 사용되는 포인터 변수

    Node *newNode = NULL;
    int readData;

    // 데이터 입력 받는 과정
    while (1)
    {
        printf("자연수 입력 : ");
        scanf("%d", &readData);
        if (readData < 1)
            break;

        // 노드 추가 과정
        newNode = (Node *)malloc(sizeof(Node)); // 노드 생성
        newNode->data = readData;               // 노드에 데이터 저장
        newNode->next = NULL;

        if (head == NULL)
            head = newNode;
        else
            tail->next = newNode;

        tail = newNode;
    }
    printf("\n");

    // 입력 받은 데이터 출력 과정
    printf("입력 받은 데이터 전체 출력 \n");
    if (head == NULL)
    {
        printf("저장된 데이터가 없습니다. \n");
    }
    else
    {
        cur = head;
        printf("%d ", cur->data); // 첫번째 데이터 출력

        // 두번째 이후의 데이터 출력
        while (cur->next != NULL) // 연결된 노드가 존재한다면
        {
            cur = cur->next;          // cur이 다음 노드를 가리키게 함
            printf("%d ", cur->data); // cur이 가리키는 노드 출력
        }
    }
    printf("\n\n");

    // 메모리의 해제과정
    if (head == NULL)
    {
        return 0; // 해제할 노드가 존재하지 않음
    }
    else
    {
        Node *delNode = head;
        Node *delNextNode = head->next;
        // head가 가리키는 노드를 그냥 삭제하면 다음 노드에 접근이 불가능하므로
        // 삭제될 노드가 가리키는 다음 노드의 주소값을 저장한다.

        printf("%d을(를) 삭제합니다. \n", head->data);
        free(delNode); // 첫번째 노드 삭제

        while (delNextNode != NULL) // 두번째 이후 노드 삭제
        {
            delNode = delNextNode;
            delNextNode = delNextNode->next;

            printf("%d을(를) 삭제합니다. \n", delNode->data);
            free(delNode);
        }
    }

    return 0;
}