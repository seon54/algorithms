#include <stdio.h>

// 이진탐색의 시간 복잡도는 최악의 경우를 기준으로
// O(log n)
int BSearch(int ar[], int len, int target)
{
    int first = 0;                      // 탐색 대상의 시작 인덱스 값
    int last = len-1;                   // 탐색 대상의 마지막 인덱스 값
    int mid;

    while(first <= last)
    {
        mid = (first+last) / 2;         // 탐색 대상의 중앙 찾기

        if(target == ar[mid])           // 중앙에 저장된 것이 타겟이면
        {
            return mid;                 // 탐색 완료
        }      
        else                            // 타겟이 아니면 탐색 댓아 반으로 줄이기
        {
            if(target < ar[mid])        
                last = mid-1;
            else
                first = mid+1;
        }
         
    }

    return -1;
}

int main(void)
{
    int arr[] = (1, 3, 5, 7, 9);
    int idx;

    idx = BSearch(arr, sizeof(arr)/sizeof(int), 7);
    if(idx == -1)
        printf("탐색 실패 \n");
    else
        printf("타켓 저장 인덱스: %d \n", idx);


    idx = BSearch(arr, sizeof(arr)/sizeof(int), 4);
    if(idx == -1)
        printf("탐색 실패 \n");
    else
        printf("타켓 저장 인덱스: %d \n", idx);
    

    return 0;
}