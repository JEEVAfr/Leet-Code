class MyHashSet:

    def __init__(self):
        self.a = set()
        

    def add(self, key: int) -> None:
        self.a.add(key)
        

    def remove(self, key: int) -> None:
        self.a.discard(key)
        

    def contains(self, key: int) -> bool:
        return key in self.a

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)