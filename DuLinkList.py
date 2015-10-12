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

    # 获取当前元素的值
    def get_data(self, index):
        current = self.__get_node(index)
        if current is None:
            return "node is not exist"
        return current.data

    # 获取当前元素的前一个元素的值
    def get_pre_data(self, index):
        current = self.__get_node(index)
        if current is None:
            return "Node is not exist"
        if current.pre is None:
            return "Node is not exist"
        return current.pre.data

    # 打印链表
    # def print_link(self):
    #     if self.is_empty():
    #         return
    #     list = []
    #     current = self.head
    #     while current.next is not None:
    #         list.append(current.data)
    #         current = current.next
    #     else:
    #         list.append(current.data)
    #     print(list)

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

    # 判断链表是否为空
    # 如果为空，返回true
    # 如果不为空，返回false
    def is_empty(self):
        return self.head is None

    # 当前元素之后插入一个元素
    # index 元素索引
    # data 插入的值
    def add_after(self, index, data):
        current = self.get_node(index)
        if current is None:
            return "node is not exist"
        current_next = current.next
        current.next = Node(data)
        current = current.next
        current.next = current_next

    # 在当前元素之前插入一个元素
    def add_before(self, index, data):
        if index == 1:
            current = self.get_node(index)
            self.head = Node(data)
            self.head.next = current
            return
        pre = self.get_pre_node(index)
        current = pre.next
        pre.next = Node(data)
        pre = pre.next
        pre.next = current

    # 获取当前元素的前一个元素
    def __get_pre_node(self, index):
        if self.is_empty():
            print("link is empty")
            return
        if index > self.get_length() or index <= 1:
            print("node is not exist")
            return
        pre = self.head
        i = 0
        while i < index:
            if i == index - 2:
                return pre
            pre = pre.next
            i += 1

    # 删除指定元素，并返回删除元素的值
    def remove(self, index):
        if index == 1 and not self.is_empty():
            data = self.head.data
            self.head = self.head.next
            return data
        pre_node = self.get_pre_node(index)
        current = self.get_node(index)
        if pre_node is None or current is None:
            print("data is not exist")
        pre_node.next = current.next
        return current.data

    # 修改当前结点的值
    def update(self, index, data):
        current = self.get_node(index)
        if current is None:
            return "current node is none"
        current.data = data

    # 将新链表合并到当前链表
    def merge(self, data):
        size = self.get_length()
        last_node = self.get_node(size)
        last_node.next = data.head
        return self

# test
s = ["a", "b", "c", "d"]
linkList = DuLinkList(s)

# print("pre:",linkList.get_pre_data(4))
linkList.print_link()