class MyHashMap:

    def __init__(self):
        self.a = defaultdict()
        

    def put(self, key: int, value: int) -> None:
        self.a[key] = value

    def get(self, key: int) -> int:
        value = self.a.get(key) 
        return value if value != None else -1
        

    def remove(self, key: int) -> None:
        self.a[key]=None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)