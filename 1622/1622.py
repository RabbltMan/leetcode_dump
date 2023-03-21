class Fancy:
    def __init__(self):
        self.fancyList = []
        self.addmul = dict()

    def append(self, val: int) -> None:
        self.fancyList.append(val)

    def addAll(self, inc: int) -> None:
        self.addmul[len(self.fancyList)] = (0, inc)

    def multAll(self, m: int) -> None:
        self.addmul[len(self.fancyList)] = (1, m)

    def getIndex(self, idx: int) -> int:
        res = self.fancyList[idx]
        if (idx >= len(self.fancyList)):
            return -1
        for key in sorted([key for key in self.addmul.keys()]):
            if idx > key:
                break
            else:
                if (self.addmul[key][0] == 0):
                    res += self.addmul[key][1]
                else:
                    res *= self.addmul[key][1]

        # print(res)
        return res

obj = Fancy()
obj.append(3)
obj.addAll(4)
obj.append(7)
obj.multAll(7)
obj.append(3)
obj.addAll(4)
obj.getIndex(0)