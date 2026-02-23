class Stack:
    def __init__(self):
        self.arr = []

    def push(self, elem):
        if self.arr:
            self.arr.append((elem, max(elem, self.arr[-1][1])))
        else:
            self.arr.append((elem, elem))
    
    def pop(self):
        if not self.arr:
            return None
        return self.arr.pop()[0]

    def get_max(self):
        if not self.arr:
            return None
        return self.arr[-1][1]
    
    def is_empty(self):
        return len(self.arr) == 0
    
    def size(self):
        return len(self.arr)
    
class Queue:
    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()
    
    def enqueue(self, elem):
        # Добавление элемента
        self.left_stack.push(elem)
    
    def dequeue(self):
        # Извлечение элемента
        if self.right_stack.is_empty():
            while not self.left_stack.is_empty():
                self.right_stack.push(self.left_stack.pop())
        
        if self.right_stack.is_empty():
            return None
        
        return self.right_stack.pop()
    
    def get_max(self):
        left_max = self.left_stack.get_max()
        right_max = self.right_stack.get_max()

        if left_max is None and right_max is None:
            return None
        elif left_max is None:
            return right_max
        elif right_max is None:
            return left_max
        else:
            return max(left_max, right_max)
        
    def size(self):
        return self.left_stack.size() + self.right_stack.size()
    
n = int(input())
A = list(map(int, input().split()))
m = int(input())

result = []
window = Queue()
for i in range(m):
    window.enqueue(A[i])

result.append(window.get_max())
for i in range(m, n):
    window.dequeue()
    window.enqueue(A[i])
    result.append(window.get_max())

print(*result)
    