'''
* when root's index is 0
parent node: (i - 1) // 2
left node: 2 * i + 1
right node: 2 + i + 2

* when root's index is 0
parent node: i // 2
left node: 2 * i
right node: 2 * i + 1
'''

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(data)

    def move_up(self, idx):
        if idx <= 0:
            return False

        parent_idx = (idx - 1) // 2
        if self.heap_array[parent_idx] < self.heap_array[idx]:
            return True
        else:
            return False

    def insert(self, data):

        # 우선 가장 마지막 인덱스에 추가
        self.heap_array.append(data)

        idx = len(self.heap_array)

        # 이동할 지 확인
        while self.move_up(data):           
            parent_idx = (idx - 1 ) // 2
            self.heap_array[idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[idx]
            idx = parent_idx

    def move_down(self, idx):
        left_idx = idx * 2 + 1
        right_idx = idx * 2 + 2

        if len(self.heap_array) <= left_idx:
            return False
        elif len(self.heap_array) <= right_idx:
            if self.heap_array[idx] < self.heap_array[left_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[right_idx] < self.heap_array[left_idx]:
                if self.heap_array[idx] < self.heap_array[left_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[idx] < self.heap_array[right_idx]:
                    return True
                else: 
                    return False

    def pop(self):
        return_data = self.heap_array[0]
        self.heap_array[0] = self.heap_array[-1]
        del self.heap_array[-1]
        idx = 0

        while self.move_down(idx):
            left_idx = idx * 2 + 1
            right_idx = idx * 2 + 2

            if len(self.heap_array) < right_idx:
                if self.heap_array[idx] < self.heap_array[left_idx]:
                    self.heap_array[idx], self.heap_array[left_idx] = self.heap_array[left_idx], self.heap_array[idx]
                    idx = left_idx
            else:
                if self.heap_array[right_idx] < self.heap_array[left_idx]:
                    if self.heap_array[idx] < self.heap_array[left_idx]:
                        self.heap_array[idx], self.heap_array[left_idx] = self.heap_array[left_idx], self.heap_array[idx]
                        idx = left_idx
                else:
                    if self.heap_array[idx] < self.heap_array[right_idx]:
                        self.heap_array[idx], self.heap_array[right_idx] = self.heap_array[right_idx], self.heap_array[idx]
                        idx = right_idx

        return return_data