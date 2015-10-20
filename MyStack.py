# coding:utf-8


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.pre = None


# 栈
class MyStack:
    def __init__(self, data=[0]):
        self.top = None
        self.init_stack(data)

    # 初始化栈
    # data 为列表元组
    def init_stack(self, data):
        if len(data) == 0:
            print("Initialization data is null")
            return
        self.top = Node(data[0])
        for index in data[1:]:
            self.push(index)

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            current = self.top
            current.next = Node(data)
            self.top = current.next
            current.next.pre = current

    def pop(self):
        if self.top is Node:
            return "stack is empty"
        data = self.top.data
        self.top = self.top.pre
        return data

    # 打印栈
    def print_queue(self):
        if self.is_empty():
            return
        alist = []
        current = self.top
        while current.pre is not None:
            alist.append(current.data)
            current = current.pre
        else:
            alist.append(current.data)
        print(alist)

    # 获取栈长度
    def get_length(self):
        if self.is_empty():
            return 0
        current = self.top
        count = 0
        while current.pre is not None:
            count += 1
            current = current.pre
        else:
            count += 1
        return count

    # 判断栈是否为空
    # 如果为空，返回true
    # 如果不为空，返回false
    def is_empty(self):
        return self.top is None


# test
# y = (1,2,3,4)
s = ["a", "b", "c", "d"]
myStack = MyStack(s)
myStack.push("x")
myStack.push("y")
myStack.push("z")


myStack.print_queue()

print("length:", myStack.get_length())
print("top:" + myStack.pop())
print("top:" + myStack.pop())
print("top:" + myStack.pop())
print("top:" + myStack.pop())

myStack.print_queue()
