#include <stdio.h>

// O(n)
int LSearch(int ar[], int len, int target)
{
    int i;
    for(i=0; i<len; i++)
    {
        if(ar[i] == target)
            return i;           // 찾은 대상의 인덱스 값 반환
    }
    return -1;                  // 못 찾음을 의미하는 값 반환
}

int main(void)
{
    int arr[] = {3, 5, 2, 4, 9};
    int idx;

    idx = LSearch(arr, sizeof(arr)/sizeof(int), 4);

    if(idx == -1)
        printf("탐색 실패 \n");
    else
        printf("타겟 저장 인덱스: %d \n", idx);

    idx = LSearch(arr, sizeof(arr)/sizeof(int), 8);

    if(idx == -1)
        printf("탐색 실패 \n");
    else
        printf("타겟 저장 인덱스: %d \n", idx);

    return 0;

}