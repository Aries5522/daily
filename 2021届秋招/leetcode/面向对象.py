class Human(object):

    def __init__(self, name):
        # 有个名字，有两只手，两条腿
        self._name = name
        self.hands = 2
        self.legs = 2

    def introduce_self(self):
        # 介绍自己
        print('我是%s' % self._name)

    def work(self):
        # 工作，但还没有定义具体的行为
        raise NotImplementedError



a=Human("小明")
b=Human("小红")
print(a._name)
class Female(Human):
    def __init__(self,name):
        super().__init__(name)
        self.hair=4
        self.power=10
        self.married=False
    def work(self):
        print("sfa")
class Male(Human):
    def __init__(self,name):
        super().__init__(name)
        self.hair = 1
        self.power = 3
        self.married = False

    def work(self):
        print('%s出去打猎了一天' % self.name)

    def marry(self, other):
        # 判断自己或对方是否已结婚，否则抛出异常
        if self.married is True or other.married is True:
            raise ValueError('法律不支持多次结婚')
        # 判断对方是否是女性，否则抛出异常
        if isinstance(other, Female):
            self.married = True
            other.married = True
        else:
            raise TypeError('法律不支持同性结婚')