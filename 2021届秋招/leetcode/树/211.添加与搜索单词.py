'''
##添加与搜索单词
'''

from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        # 当前节点的子树节点
        self.children = defaultdict(TrieNode)
        # 从根节点到该节点的路径是否一个单词
        self.is_word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 字典树的根节点
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        # 从根节点开始遍历
        cur_node = self.root
        # 每个字符是一个节点，如果没有则新建，有则直接向下遍历继续插入
        for ch in word:
            cur_node = cur_node.children[ch]
        # 整个单词中的每个字符都对应有一个节点了，并且是通过children关联起来的，
        # 那么这最后一个字符的节点就表示一个单词的结尾
        cur_node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        # 从根节点向下遍历
        cur_node = self.root

        # 因为需要支持通配符，当遇到通配符时，需要遍历当前节点的所有子节点
        # 因此这里需要采用一个辅助递归函数
        def _helper(node, _word, index):
            if index == len(_word):
                return node.is_word

            cur_node = node
            ch = _word[index]
            # 如果当前字符为通配符
            if ch == ".":
                # 遍历当前节点的所有子节点
                for _node in cur_node.children.values():
                    # 递归调用：查看当前字符之后的子字符串跟后续的节点路径是否匹配，
                    # 如果有一条路径是匹配的，则表示整个通配符字符串匹配成功
                    if _helper(_node, _word, index + 1):
                        return True
                # 所有的子节点路径跟当前的字符串均不匹配
                return False
            else:
                # 如果是普通字符，精确匹配该字符是否存在节点
                cur_node = cur_node.children.get(ch)
                # 不存在则表示不匹配
                if not cur_node:
                    return False
                # 存在，继续递归后续的子字符串
                return _helper(cur_node, _word, index + 1)

        return _helper(cur_node, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("a")
obj.addWord("a")
obj.addWord("apple")
print(obj.search("a."), obj.search(".app"))
