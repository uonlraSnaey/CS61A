import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Node():
    def __init__(self, data=None):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    def __str__(self):
        return 'Node:<data: %s><quote: %s>' % (self._data, self._next)


class LinkedList():
    def __init__(self):  # head.data=length of the linkedlist
        self._head = Node(0)
        self._tail = self._head

    def __len__(self):
        return self._head.data

    def __bool__(self):
        return bool(self._head.data)

    def __str__(self):
        linkedlist = self._data2list()
        return 'linkedlist: %s' % str(linkedlist)  # 将str的打印方式委托给了list的__str__

    def __contains__(self, value):
        linkedlist = self._data2list()
        return value in linkedlist

    def generate_node(self):
        node = self._head.next
        while node != None:
            yield node
            node = node.next

    def _data2list(self):
        if self._head.data == 0:
            return []
        else:
            return [x.data for x in self.generate_node()]

    def add(self, value):  # 尾部增加
        node = Node(value)
        self._tail.next = node
        self._tail = node
        self._head.data += 1

    def pop(self, value):
        assert self.__contains__(value) == True, 'there is no value %s' % value
        if value == self._head.next.data:
            self._head.next = self._head.next.next
        else:
            nodes = list(self.generate_node())  # list代码清晰，但是空间会占用大些
            for index in range(self.__len__):
                cur_node = nodes[index]
                if cur_node.data == value:
                    pre_node = nodes[index - 1]
                    if index == self._length - 1:
                        next_node = None
                    else:
                        next_node = nodes[index + 1]
                    logger.info('the data: %s has been deleted, and the pre node is %s' %
                                (cur_node.data, pre_node.data))
                    pre_node.next = next_node

    def superpop(self, node):
        assert node.next != None, 'must not be the tail'
        node.data = node.next.data
        node.next = node.next.next


def main():
    x = LinkedList()
    for i in range(5):
        x.add(i)
    print('length % 2d, the data is %s' % (len(x), x))
    x.pop(0)
    print(x)


if __name__ == '__main__':
    main()
