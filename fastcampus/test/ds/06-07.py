'''
[int]
- 수의 제한이 없다
- 문자열에서 숫자로 쉽게 바꿀 수 있음 str('123')
- 나눗셈 주의
    - 4 // 2
    - divmod(4, 2)  => 2, 0

[float]
- 연산에서 사용 X
- 유리수 연산은 tuple로 분자, 분모 따로 처리

[string]
- 변경할 수 없는 변수 => list로 변환해서 사용
- '+', '*' 연산 조심 => join() 활용   ex1. 참고
- split(), replace() 등 메소드 활용
- slicing 자유롭게 할 수 있어야 함  => 슬라이싱을 하게 되면 새로운 객체를 생성하게 되는 점 기억
- char 를 ord 와 chr 로 다루기

[bool]
- 논리 연산과 활용
- short circuit (조건 순서 !!)
    - or 연산 앞에 항이 참
    - and 연산 앞에 항이 거짓

[list]
- list comperhension
- sort(객체의 정렬 변환), sorted(리스트를 정렬한 새 객체 반환) 구분
- len, sum, max, min 활용
- slicing, [-1] 등의 음수 인덱스 활용
- reduce, filter 활용

[tuple]
- 초기 상태 표현시 코드가 길어지는 것 방지
  ex. a, b,c = 0, 0, 0
- map과 함께 사용하여 입력 받기
  ex. a, b = map(int, input().split())
- 동시에 변해야하는 객체에 효율적 표현 가능
  ex. a, b = b, a

[dictionary]
- keys(), values() 사용하여 효율적 사용 추천
- 반복문 돌리기
- 문자열 자체를 인덱스로 사용하고 싶은 경우
  ex. 단어나, 알파벳 개수 세기
- collections.Counter

[set]
- 중복 체크
  ex.set(list)
- 합집합, 여집합, 차집합 등의 집합 연산  * 시간복잡도가 크므로 주의해서 사용

[heap]
- heapq (기본 최소힙)
- 최대힙으로 이용할 때는 -1 곱해서 사용
'''

# str ex1.

s1 = ''

for i in range(10000):
    s = s + str(i)

s2 = ''

s2 = s2.join([str(i) for i in range(10000)])