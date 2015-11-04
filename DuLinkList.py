# coding:utf-8
from LinkList import LinkList

class Node:
    def __init__(self, value):
        self.data = value
        self.pre = None
        self.next = None


# 双向链表
class DuLinkList(LinkList):
    def __init__(self, data=[0]):
        self.head = None
        self.init_link_list(data)

    # 初始化链表
    # data 为数组
    def init_link_list(self, data):
        if len(data) == 0:
            print("Initialization data is null")
            return
        self.head = Node(data[0])
        current = self.head
        for index in data[1:]:
            current.next = Node(index)
            current.next.pre = current
            current = current.next

    # 获取当前结点
    def __get_node(self, index):
        if self.is_empty():
            print("link is empty")
            return
        if index > self.get_length() or index <= 0:
            print("node is not exist")
            return
        current = self.head
        i = 0
        while i < index:
            if i == index - 1:
                return current
            current = current.next
            i += 1

    # 获取当前元素的前一个元素的值
    def get_pre_data(self, index):
        current = self.__get_node(index)
        if current is None:
            return "Node is not exist"
        if current.pre is None:
            return "Node is not exist"
        return current.pre.data

    # 当前元素之后插入一个元素
    # index 元素索引
    # data 插入的值
    def add_after(self, index, data):
        current = self.__get_node(index)
        if current is None:
            return "node is not exist"
        if index == self.get_length():
            current.next = Node(data)
            current.next.pre = current
        else:
            current_next = current.next
            current.next = Node(data)
            current.next.pre = current
            current = current.next
            current_next.pre = current.next
            current.next = current_next

    # 在当前元素之前插入一个元素
    def add_before(self, index, data):
        if index == 1:
            current = self.__get_node(index)
            self.head = Node(data)
            current.pre = self.head
            self.head.next = current
        else:
            pre = self.__get_node(index).pre
            current = self.__get_node(index)
            current.pre = Node(data)
            pre.next = current.pre
            current.pre.pre = pre
            current.pre.next = current

    # 删除指定元素，并返回删除元素的值
    def remove(self, index):
        if index == 1 and not self.is_empty():
            data = self.head.data
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.pre = None
            return data
        pre_node = self.__get_node(index).pre
        next_node = self.__get_node(index).next
        current_data = self.get_data(index)
        pre_node.next = next_node
        if next_node is not None:
            next_node.pre = pre_node
        return current_data

    # 修改当前结点的值
    def update(self, index, data):
        current = self.get_node(index)
        if current is None:
            return "current node is none"
        current.data = data

    # 将新链表合并到当前链表
    def merge(self, data):
        size = self.get_length()
        last_node = self.__get_node(size)
        last_node.next = data.head
        data.head.pre = last_node
        return self

# test
s = ["a", "b", "c", "d"]
linkList = DuLinkList(s)
# print("length:", linkList.get_length())

# print("pre:",linkList.get_pre_data(4))
# print("data:", linkList.get_data(3))
# print("pre data:", linkList.get_pre_data(3))
# linkList.add_after(4,"x")
# print(linkList.get_pre_data(5))
# linkList.add_before(4,"x")
# print("pre:", linkList.get_pre_data(1))
# linkList.remove(1)
# print("pre:", linkList.get_pre_data(1))

y = [1, 2, 3]
se = DuLinkList(y)
linkList.merge(se)
linkList.print_link()