from collections import defaultdict


'''字典树'''
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.temp={}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        tree=self.temp ##(一定要重新给,不能直接操作self变量)
        for a in word:
            if a not in tree:
                tree[a]={}
            tree=tree[a]
        tree["#"]="#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree=self.temp
        for a in word:
            if a not in tree:
                return False
            else:
                tree=tree[a]
        if "#" in tree:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree=self.temp
        for a in prefix:
            if a not in tree:
                return False
            else:
                tree=tree[a]
        return True


trie = Trie()

trie.insert("apple")
trie.insert("beer")
trie.insert("add")
trie.insert("jam")
trie.insert("rental")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
