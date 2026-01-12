class Trie:

    def __init__(self):
        self.set=set()
        self.pre=set()

    def insert(self, word: str) -> None:
        self.set.add(word)
        for i in range(len(word)):
            self.pre.add(word[:i+1])
    def search(self, word: str) -> bool:
        if word in self.set:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.pre:
            return True
        else:
            return False
        

