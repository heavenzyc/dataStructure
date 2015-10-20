# coding:utf-8


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# 单链表
class MyQueue:
    def __init__(self, data=[0]):
        self.head = None
        self.init_queue(data)

    # 初始化队列
    # data 为列表元组
    def init_queue(self, data):
        if len(data) == 0:
            print("Initialization data is null")
            return
        self.head = Node(data[0])
        current = self.head
        for index in data[1:]:
            current.next = Node(index)
            current = current.next

    def input_queue(self, data):
        if self.head is None or self.is_empty():
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            else:
                current.next = Node(data)

    def out_queue(self):
        if self.head is None:
            return "queue is empty"
        data = self.head.data
        current = self.head
        self.head = current.next
        return data

    # 打印链表
    def print_queue(self):
        if self.is_empty():
            return
        alist = []
        current = self.head
        while current.next is not None:
            alist.append(current.data)
            current = current.next
        else:
            alist.append(current.data)
        print(alist)

    # 获取链表长度
    def get_length(self):
        if self.is_empty():
            return 0
        current = self.head
        count = 0
        while current.next is not None:
            count += 1
            current = current.next
        else:
            count += 1
        return count

    # 判断队列是否为空
    # 如果为空，返回true
    # 如果不为空，返回false
    def is_empty(self):
        return self.head is None


# test
# y = (1,2,3,4)
s = ["a", "b", "c", "d"]
myQueue = MyQueue(s)
print("output:"+myQueue.out_queue())
myQueue.input_queue("x")
myQueue.input_queue("y")
myQueue.input_queue("z")


myQueue.print_queue()
