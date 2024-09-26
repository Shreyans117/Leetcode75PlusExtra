class Node:
    def __init__(self, key: int, value:int):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            if self.head!=node:
                if self.tail==node:
                    self.tail=self.tail.prev
                    self.tail.next=None
                else:
                    node.prev.next=node.next
                    node.next.prev=node.prev
                node.next=self.head
                self.head.prev=node
                node.prev=None
                self.head=node
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.get(key)
            self.head.value=value
        elif self.size<self.capacity:
            node = Node(key, value)
            self.size+=1
            if self.tail==None:
                self.tail=self.head=node
            elif self.tail.prev==None:
                node.next=self.head
                self.head.prev=node
                self.tail=self.head
                self.head=node
            else:
                node.next=self.head
                self.head.prev=node
                self.head=node
            self.cache[key] = node

        else:
            node = Node(key, value)
            evict=self.tail
            if self.tail!=self.head:
                self.tail=self.tail.prev
            if self.tail:
                self.tail.next=None
            evict.prev=None
            self.cache.pop(evict.key, None)
            node.next=self.head
            self.head.prev=node
            self.head = node
            self.cache[key] = node
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)