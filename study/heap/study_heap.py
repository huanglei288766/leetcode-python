import heapq

class MaxHeap:

    def __init__(self, heap_size: int):
        self.realSize = 0
        self.heapSize = heap_size
        self.heap = [0] * (heap_size + 1)

    def push(self, item):
        if self.realSize == self.heapSize:
            raise 'MaxHeap index out of range'

        self.realSize += 1
        self.heap[self.realSize] = item

        cur = self.realSize
        while cur > 1:
            parent = cur // 2
            if self.heap[parent] < self.heap[cur]:
                self.heap[cur], self.heap[parent] = self.heap[parent], self.heap[cur]
            else:
                break
            cur = parent

    def pop(self):
        if self.realSize == 0:
            raise IndexError('MaxHeap index out of range')

        pop = self.heap[1]
        self.heap[1] = self.heap[self.realSize]
        self.realSize -= 1
        if self.realSize == 0:
            return pop

        cur = 1
        while cur < self.realSize // 2:
            left = cur * 2
            right = cur * 2 + 1
            if self.heap[cur] < self.heap[left] or self.heap[cur] < self.heap[right]:
                if self.heap[left] > self.heap[right]:
                    self.heap[cur], self.heap[left] = self.heap[left], self.heap[cur]
                    cur = left
                else:
                    self.heap[cur], self.heap[right] = self.heap[right], self.heap[cur]
                    cur = right
        return pop

if __name__ == '__main__':
    minheap = [1, 2, 3]
    heapq.heapify(minheap)
    heapq.heappush(minheap, 4)
    print(minheap)
    print(minheap)