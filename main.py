# Intern
import time
from collections import deque
import random


# 1 Task
def is_Even(value):
    return list(map(int, str(value)))[-1] % 2 == 0


def isEven(value):
    return value % 2 == 0


start = time.perf_counter()
print(is_Even(30120301209309120912903901290302103021001202021212121989812982189128919821))
finish = time.perf_counter()
print('Время работы 1 функции: ' + str(finish - start))
start = time.perf_counter()
print(isEven(30120301209309120912903901290302103021001202021212121989812982189128919821))
finish = time.perf_counter()
print('Время работы 2 функции: ' + str(finish - start))
"""
Моя функция в среднем быстрее в два раза, так как для проверки четности достаточно проверить последнюю цифру на четность, 
однако такое решение занимает больше памяти
"""


# 2 Task
class CircularBufferLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.size = 0
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            self.dequeue()
        if len(self.buffer) < self.capacity:
            self.buffer.append(value)
            self.size += 1
        else:
            self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity

    def dequeue(self):
        if self.size == 0:
            return None
        value = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value


class CircularBufferDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def enqueue(self, value):
        self.buffer.append(value)

    def dequeue(self):
        if len(self.buffer) == 0:
            return None
        return self.buffer.popleft()


'''
Сравнение реализаций:
Плюсы реализации CircularBufferLinkedList:
- Простая реализация с использованием списка
- Может быть более эффективной при малом размере буфера
Минусы реализации CircularBufferLinkedList:
- Возможно неэффективное удаление элементов из начала буфера при большом размере

Плюсы реализации CircularBufferDeque:
- Использование deque для поддержки циклического буфера
- Эффективное удаление элементов из начала буфера
- Удобные методы append и popleft
Минусы реализации CircularBufferDeque:
- Немного сложнее в понимании из-за использования deque, так как не видно сразу что происходит под капотом
'''

#3 Task
'''
Самым быстрым алгоритмом является Timsort поэтому достаточно было бы использовать встроенную функцию сортировки
'''


def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        arr[i:i + min_run] = sorted(arr[i:i + min_run])

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            arr[start: start + size * 2] = sorted(arr[start: start + size] + arr[start + size: start + size * 2])
        size *= 2

    return arr


# Пример использования
arr = [random.randint(1, 1000) for i in range(100)]
sorted_arr = timsort(arr)
print(sorted_arr)
