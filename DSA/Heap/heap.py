# implementation of heap 

class MinHeap :

    def __init__(self):
        self.heap = []
    

    # heapify up 
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    # heapify down 
    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
    
    # insert 
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def delete(self, value):
        if not self.heap:
            return None

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root 
    
    def display(self):
        print(self.heap)


class MaxHeap:

    def __init__(self):
        self.heap = []

    
    def _heapify_down(self, index):
        largest = index
        left = index * 2 + 1
        right = index * 2 + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < len(self.heap) and self.heap[right] > self.head[largest]:
            largest = right
        
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self._heapify_down(largest)
    

    def _heapify_up(self, index):
        parent = index + 1 // 2
        while parent > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index + 1) // 2
    
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def delete(self):
        if not self.heap:
            return 
        root = self.heap[0]
        self.head[0] = self.heap.pop()
        self._heapify_down(0)
        return root


# Example Usage
if __name__ == "__main__":
    print("Min Heap Example:")
    min_heap = MinHeap()
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(8)
    min_heap.insert(1)
    min_heap.display()

        