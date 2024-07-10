from collections import deque

antrian = deque()

def enqueue(item):
    antrian.append(item)
    # antrian.appendleft(item)
def dequeue():
    antrian.popleft()

def front():
    return antrian[0]

enqueue('wildan')
enqueue('putra')
enqueue('samaul')
enqueue('YanTa')
dequeue()
front()
print(antrian)